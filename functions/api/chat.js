/**
 * Chat2KB Chat API (Cloudflare Pages Function)
 *
 * - 通用 / 知识库问题：直接调用 Kimi (Moonshot) 大模型
 * - dev 环境运营问题：使用 Digest 认证（accessKey:secretKey）调用 ApeCloud admin API，
 *   根据用户问题动态选择多个 endpoint 获取实时数据，再交给 Kimi 总结
 *
 * 依赖环境变量（通过 .dev.vars 或 wrangler secret 配置）：
 *   KIMI_API_KEY
 *   ADMIN_DEV_API_BASE       例如 https://api-dev.apecloud.cn/admin/v1/
 *   ADMIN_DEV_ACCESS_KEY     API Key 的 accessKey（Digest 用户名）
 *   ADMIN_DEV_SECRET_KEY     API Key 的 secretKey（Digest 密码）
 *
 * 认证文档：
 *   https://console-dev.apecloud.cn/docs/developer-guides/api/adminapi/admin-api
 */

import md5 from '../../lib/md5.js';

const KIMI_BASE = 'https://api.moonshot.cn/v1';
const KIMI_MODEL = 'kimi-k2.5';

function jsonResponse(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}

// ─── Digest Auth fetch helper ───
function parseDigestParams(header) {
  const params = {};
  const regex = /(\w+)=((?:"[^"]*")|[^,\s]+)/g;
  let m;
  while ((m = regex.exec(header)) !== null) {
    let val = m[2];
    if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
    params[m[1]] = val;
  }
  return params;
}

function randomHex(len) {
  const arr = new Uint8Array(len / 2);
  crypto.getRandomValues(arr);
  return Array.from(arr, (b) => b.toString(16).padStart(2, '0')).join('');
}

async function digestFetch(url, method, username, password) {
  const first = await fetch(url, { method });
  if (first.status !== 401) return first;

  const wwwAuth = first.headers.get('www-authenticate');
  if (!wwwAuth || !wwwAuth.toLowerCase().startsWith('digest ')) return first;

  const p = parseDigestParams(wwwAuth);
  const realm = p.realm;
  const nonce = p.nonce;
  const opaque = p.opaque || '';
  const qop = p.qop || 'auth';
  const algorithm = p.algorithm || 'MD5';
  const cnonce = randomHex(32);
  const nc = '00000001';
  const uri = new URL(url).pathname + new URL(url).search;

  const ha1 = md5(`${username}:${realm}:${password}`);
  const ha2 = md5(`${method}:${uri}`);
  const response = md5(`${ha1}:${nonce}:${nc}:${cnonce}:${qop}:${ha2}`);

  const authHeader = `Digest username="${username}", realm="${realm}", nonce="${nonce}", uri="${uri}", cnonce="${cnonce}", nc=${nc}, qop=${qop}, response="${response}", opaque="${opaque}", algorithm=${algorithm}`;

  return fetch(url, {
    method,
    headers: {
      Authorization: authHeader,
      Accept: 'application/json',
    },
  });
}

// ─── Admin API endpoint selection ───
const ADMIN_ENDPOINTS = [
  {
    path: '/organizations',
    keywords: ['组织', 'organization', 'org', '客户', '注册', 'company', '租户', 'tenant'],
    default: true,
  },
  {
    path: '/clusters',
    keywords: ['集群', 'cluster', '实例', 'instance', '数据库', 'database'],
    default: true,
  },
  {
    path: '/environments',
    keywords: ['环境', 'environment', 'env', '节点', 'node', '资源', 'resource'],
    default: false,
  },
  {
    path: '/users',
    keywords: ['用户', 'user', '账号', 'account', '成员', 'member', '登录', '活跃', '沉默'],
    default: false,
  },
  {
    path: '/tasks',
    keywords: ['任务', 'task', '作业', 'job', '运维', 'operation'],
    default: false,
  },
  {
    path: '/events',
    keywords: ['事件', 'event', '告警', 'alert', '日志', 'log', '通知'],
    default: false,
  },
  {
    path: '/bills',
    keywords: ['账单', 'bill', '费用', 'cost', '成本', 'billing', '计费'],
    default: false,
  },
  {
    path: '/backup-repos',
    keywords: ['备份', 'backup', '仓库', 'repo', '恢复', 'restore'],
    default: false,
  },
  {
    path: '/alert-rules',
    keywords: ['告警规则', 'alert rule', '告警策略', 'alert strategy'],
    default: false,
  },
  {
    path: '/engine-options',
    keywords: ['引擎', 'engine', '版本', 'version', '配置', 'parameter'],
    default: false,
  },
];

function selectEndpoints(query) {
  const q = query.toLowerCase();
  const scored = ADMIN_ENDPOINTS.map((ep) => {
    const score = ep.keywords.reduce((s, kw) => (q.includes(kw.toLowerCase()) ? s + 1 : s), 0);
    return { ...ep, score };
  });

  // 默认始终拉取 /organizations 和 /clusters；再按关键词匹配追加前 3 个相关 endpoint
  const selected = new Set(ADMIN_ENDPOINTS.filter((ep) => ep.default).map((ep) => ep.path));
  const matched = scored
    .filter((ep) => ep.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 3);
  matched.forEach((ep) => selected.add(ep.path));
  return Array.from(selected);
}

async function fetchDevAdminData(env, query) {
  const base = (env.ADMIN_DEV_API_BASE || 'https://api-dev.apecloud.cn/admin/v1/').replace(/\/$/, '');
  const username = env.ADMIN_DEV_ACCESS_KEY;
  const password = env.ADMIN_DEV_SECRET_KEY;

  if (!username || !password) {
    throw new Error('ADMIN_DEV_ACCESS_KEY / ADMIN_DEV_SECRET_KEY 未配置');
  }

  const paths = selectEndpoints(query);
  const results = {};

  await Promise.all(
    paths.map(async (path) => {
      const url = `${base}${path}`;
      try {
        const resp = await digestFetch(url, 'GET', username, password);
        if (resp.ok) {
          const data = await resp.json();
          results[path] = data;
        } else {
          const errText = await resp.text();
          console.warn(`admin-dev API ${path} 失败: ${resp.status} ${errText}`);
          results[path] = { error: `${resp.status}: ${errText}` };
        }
      } catch (e) {
        console.warn(`admin-dev API ${path} 异常:`, e.message);
        results[path] = { error: e.message };
      }
    })
  );

  return results;
}

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.KIMI_API_KEY) {
    return jsonResponse({ error: 'KIMI_API_KEY 未配置' }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch (e) {
    return jsonResponse({ error: '请求体 JSON 解析失败' }, 400);
  }

  const { env: userEnv, query } = body;
  if (!query || typeof query !== 'string') {
    return jsonResponse({ error: '缺少 query 参数' }, 400);
  }

  let systemPrompt = `你是 Chat2KB，一个面向 KubeBlocks 生态的对话式数据库智能助手。

你的能力：
1. 知识库问答：回答 KubeBlocks、MySQL、PostgreSQL、Redis 等数据库相关的产品文档、最佳实践、故障排查问题。
2. 运营洞察：当用户询问 dev / apecloud.cn / kubeblocks.io 等 Demo 环境的数据时，基于提供的实时数据给出简洁、结构化的分析。

回答要求：
- 用中文回答。
- 给出结论前先列出关键数据点。
- 涉及对比、排名、利用率时使用列表或表格形式。
- 如果数据不足，明确说明并给出建议。`;

  let adminData = null;
  let adminDataOk = false;

  if (userEnv === 'dev' && env.ADMIN_DEV_API_BASE) {
    try {
      adminData = await fetchDevAdminData(env, query);
      // 只要有一个 endpoint 成功就算可用
      adminDataOk = Object.values(adminData).some((v) => !v.error);
    } catch (e) {
      console.warn('admin-dev API 请求异常:', e.message);
    }
  }

  if (adminDataOk && adminData) {
    systemPrompt += `\n\n[dev 环境实时数据]\n${JSON.stringify(adminData, null, 2)}\n\n请基于以上数据回答用户关于 dev 环境的问题。`;
  } else if (userEnv === 'dev') {
    systemPrompt += `\n\n注意：当前 dev 环境的实时数据接口未配置或暂时不可用，请基于你的知识回答，并提示用户检查 ADMIN_DEV_ACCESS_KEY / ADMIN_DEV_SECRET_KEY。`;
  }

  const messages = [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: query },
  ];

  try {
    const kimiResp = await fetch(`${KIMI_BASE}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${env.KIMI_API_KEY}`,
      },
      body: JSON.stringify({
        model: KIMI_MODEL,
        messages,
        temperature: 1,
        stream: false,
      }),
    });

    if (!kimiResp.ok) {
      const errText = await kimiResp.text();
      console.error('Kimi API error:', kimiResp.status, errText);
      return jsonResponse(
        { error: `Kimi API 请求失败: ${kimiResp.status}` },
        502
      );
    }

    const data = await kimiResp.json();
    const content = data.choices?.[0]?.message?.content || '';

    return jsonResponse({
      content,
      env: userEnv,
      source: adminDataOk ? 'kimi+admin-dev' : 'kimi',
      adminData: adminDataOk ? adminData : undefined,
    });
  } catch (e) {
    console.error('调用 Kimi 时发生异常:', e);
    return jsonResponse({ error: `调用 Kimi 时发生异常: ${e.message}` }, 502);
  }
}
