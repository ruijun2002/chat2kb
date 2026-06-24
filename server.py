#!/usr/bin/env python3
"""
Chat2KB local development server.

Serves static files (index.html, chat.html, changelog.html, etc.) and handles
POST /api/chat by calling Kimi (Moonshot) and the ApeCloud dev admin API.

Usage:
    python3 server.py 8080

Then open http://localhost:8080/chat.html?env=dev
"""

import argparse
import json
import os
import re
import sqlite3
import subprocess
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, urlencode

# ─── Config ───
DEFAULT_PORT = 8080
DEV_API_BASE = "https://api-dev.apecloud.cn/admin/v1/"
KIMI_BASE = "https://api.moonshot.cn/v1"
DEEPSEEK_BASE = "https://api.deepseek.com/v1"
KIMI_MODEL = "kimi-k2.5"

# Which admin endpoints to query, and keywords that trigger them
ADMIN_ENDPOINTS = [
    {
        "path": "/organizations",
        "keywords": ["组织", "organization", "org", "客户", "注册", "company", "租户", "tenant"],
        "default": True,
    },
    {
        "path": "/clusters",
        "keywords": ["集群", "cluster", "实例", "instance", "数据库", "database"],
        "default": True,
    },
    {
        "path": "/environments",
        "keywords": ["运行环境", "环境列表", "环境数量", "环境统计", "environment list", "environments", "节点", "node", "资源", "resource"],
        "default": False,
    },
    {
        "path": "/users",
        "keywords": ["用户", "user", "账号", "account", "成员", "member", "登录", "活跃", "沉默"],
        "default": False,
    },
    {
        "path": "/tasks",
        "keywords": ["任务", "task", "作业", "job", "运维", "operation"],
        "default": False,
    },
    {
        "path": "/events",
        "keywords": ["事件", "event", "告警", "alert", "日志", "log", "通知"],
        "default": False,
    },
    {
        "path": "/bills",
        "keywords": ["账单", "bill", "费用", "cost", "成本", "billing", "计费"],
        "default": False,
    },
    {
        "path": "/backup-repos",
        "keywords": ["备份", "backup", "仓库", "repo", "恢复", "restore"],
        "default": False,
    },
    {
        "path": "/alert-rules",
        "keywords": ["告警规则", "alert rule", "告警策略", "alert strategy"],
        "default": False,
    },
    {
        "path": "/engine-options",
        "keywords": ["引擎", "engine", "版本", "version", "配置", "parameter"],
        "default": False,
    },
]


def load_dev_vars():
    """Load key=value pairs from .dev.vars if present."""
    env = dict(os.environ)
    dev_vars = Path(__file__).parent / ".dev.vars"
    if dev_vars.exists():
        for line in dev_vars.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


ENV = load_dev_vars()

# ─── Admin API catalog for LLM-driven workflow ───
def load_api_catalog():
    catalog_path = Path(__file__).parent / "api_catalog.json"
    if not catalog_path.exists():
        return []
    try:
        return json.loads(catalog_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Failed to load api_catalog.json: {e}")
        return []


API_CATALOG = load_api_catalog()


def load_readonly_api_ids():
    """Parse ReadonlyAPI.md and return the set of allowed read-only operationIds."""
    readonly_path = Path(__file__).parent / "ReadonlyAPI.md"
    if not readonly_path.exists():
        return set()
    ids = set()
    for line in readonly_path.read_text(encoding="utf-8").splitlines():
        if "`GET`" not in line:
            continue
        m = re.search(r"`([^`]+)`\s*\|\s*`GET`", line)
        if m:
            ids.add(m.group(1))
    return ids


READONLY_IDS = load_readonly_api_ids()


def load_adminapi_overview():
    """Load the human-readable admin API overview for LLM planning."""
    overview_path = Path(__file__).parent / "adminapi-overview.md"
    if not overview_path.exists():
        return ""
    try:
        return overview_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Failed to load adminapi-overview.md: {e}")
        return ""


ADMINAPI_OVERVIEW = load_adminapi_overview()

# ─── SQLite settings persistence ───
DB_PATH = Path(__file__).parent / "chat2kb.db"

SETTING_KEYS = [
    "adminBase",
    "adminAccessKey",
    "adminSecretKey",
    "llmModel",
    "llmApiId",
    "llmApiKey",
    "llmBase",
]


def resolve_llm_base(model: str, base_override: str = "") -> str:
    """Return the appropriate base URL for a model."""
    if base_override:
        return base_override.rstrip("/")
    if not model:
        return KIMI_BASE
    if model.lower().startswith("deepseek"):
        return DEEPSEEK_BASE
    return KIMI_BASE


def default_settings():
    """Return default settings, preferring values from .dev.vars when present."""
    # Prefer an explicit LLM_* config over the legacy KIMI_API_KEY
    llm_api_key = ENV.get("LLM_API_KEY") or ENV.get("DEEPSEEK_API_KEY") or ENV.get("KIMI_API_KEY", "")
    llm_model = ENV.get("LLM_MODEL") or "kimi-k2.6"
    llm_base = ENV.get("LLM_BASE") or resolve_llm_base(llm_model)
    return {
        "adminBase": ENV.get("ADMIN_DEV_API_BASE") or DEV_API_BASE,
        "adminAccessKey": ENV.get("ADMIN_DEV_ACCESS_KEY", ""),
        "adminSecretKey": ENV.get("ADMIN_DEV_SECRET_KEY", ""),
        "llmModel": llm_model,
        "llmApiId": "",
        "llmApiKey": llm_api_key,
        "llmBase": llm_base,
    }


def init_db():
    """Create the settings table and pre-fill / refresh defaults from .dev.vars."""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
        )
        existing = {row[0] for row in conn.execute("SELECT key FROM settings")}
        defaults = default_settings()
        for key, value in defaults.items():
            if key not in existing:
                conn.execute(
                    "INSERT INTO settings (key, value) VALUES (?, ?)",
                    (key, value),
                )
            elif value:
                # If a setting is currently empty but .dev.vars provides a value, refill it.
                conn.execute(
                    "UPDATE settings SET value = ? WHERE key = ? AND (value IS NULL OR value = '')",
                    (value, key),
                )
        conn.commit()
    finally:
        conn.close()


def get_settings():
    """Load all settings from SQLite as a dict."""
    conn = sqlite3.connect(DB_PATH)
    try:
        rows = conn.execute("SELECT key, value FROM settings").fetchall()
        return {row[0]: row[1] for row in rows}
    finally:
        conn.close()


def save_settings(settings: dict):
    """Upsert settings into SQLite."""
    conn = sqlite3.connect(DB_PATH)
    try:
        for key in SETTING_KEYS:
            value = settings.get(key, "")
            conn.execute(
                "INSERT INTO settings (key, value) VALUES (?, ?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                (key, value),
            )
        conn.commit()
    finally:
        conn.close()



# ─── curl helpers (macOS/Linux have curl; avoids Python urllib TLS quirks) ───
def curl(args: list, timeout: int = 30):
    """Run curl and return (exit_code, stdout, stderr)."""
    cmd = ["curl", "-sS", "--fail-with-body"] + args
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return 28, "", "curl: timeout"
    except FileNotFoundError:
        return 127, "", "curl not found"


def digest_curl(url: str, username: str, password: str):
    """Fetch a Digest-auth URL using curl. Returns (http_status, body)."""
    code, out, err = curl([
        "--max-time", "20",
        "--digest",
        "-u", f"{username}:{password}",
        "-H", "Accept: application/json",
        "-w", "\\n%{http_code}",
        url,
    ], timeout=30)
    # -w appends the status code as the last line of stdout
    status = 0
    body = out
    lines = out.rsplit("\n", 1)
    if len(lines) == 2:
        try:
            status = int(lines[-1].strip())
            body = lines[0]
        except ValueError:
            pass
    if status == 0 and code != 0:
        # curl failed before we got a status line; try to extract HTTP code from stderr
        m = re.search(r"returned error: (\d{3})", err)
        if m:
            status = int(m.group(1))
            body = err
    return status, body or err


def llm_curl(api_key: str, base: str, payload: dict):
    """POST to an OpenAI-compatible chat completions endpoint. Returns dict with content or error."""
    body = json.dumps(payload, ensure_ascii=False)
    code, out, err = curl([
        "--max-time", "60",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {api_key}",
        "-d", body,
        f"{base}/chat/completions",
    ], timeout=70)
    if code != 0:
        return {"error": f"LLM API 错误: {code} {err or out}"}
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return {"error": f"LLM API 返回非 JSON: {out[:200]}"}
    if data.get("error"):
        return {"error": f"LLM API 错误: {data['error']}"}
    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    return {"content": content}


def test_admin_connection(base: str, username: str, password: str):
    """Test dev admin API connectivity. Returns (ok, error_message)."""
    base = base.rstrip("/")
    url = f"{base}/organizations"
    status, body = digest_curl(url, username, password)
    if status == 200:
        return True, ""
    return False, f"连接失败 (HTTP {status}): {body[:200]}"


def test_llm_connection(api_key: str, model: str = None, base: str = None):
    """Test LLM API key. Try /models first, then a minimal chat completion as fallback."""
    base = resolve_llm_base(model, base or "")
    code, out, err = curl([
        "--max-time", "20",
        "-H", f"Authorization: Bearer {api_key}",
        f"{base}/models",
    ], timeout=30)
    if code == 0:
        return True, ""

    primary_err = (err or out)[:300]
    print(f"LLM /models test failed ({base}): {primary_err}")

    # If /models returns 401, try a minimal chat completion to verify the key itself.
    if "401" in primary_err:
        test_model = model if model and model != "custom" else "kimi-k2.5"
        if base == DEEPSEEK_BASE and not test_model.startswith("deepseek"):
            test_model = "deepseek-v4-pro"
        body = json.dumps({
            "model": test_model,
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 1,
        }, ensure_ascii=False)
        code2, out2, err2 = curl([
            "--max-time", "20",
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {api_key}",
            "-d", body,
            f"{base}/chat/completions",
        ], timeout=30)
        print(f"LLM /chat/completions fallback test ({base}): code={code2}, err={err2[:200]}")
        if code2 == 0:
            return True, ""
        return False, f"认证失败: {(err2 or out2)[:300]}"

    return False, f"请求失败: {primary_err}"


def select_endpoints(query: str):
    """Pick admin endpoints to query based on the user question.

    - If the question clearly points to a single endpoint, return only that endpoint.
    - Otherwise return all positively-scored endpoints, sorted by relevance.
    - Fall back to the default endpoints only when nothing specific is matched.
    """
    q = query.lower()

    # Strong single-intent patterns: when these are present, avoid broad defaults.
    strong_patterns = {
        "/clusters": ["集群数", "集群数量", "集群统计", "cluster count", "clusters", "有多少个集群", "集群列表"],
        "/organizations": ["组织数", "组织数量", "组织统计", "organization count", "organizations", "有多少组织", "客户数", "客户数量"],
        "/environments": ["环境数", "环境数量", "环境统计", "environment count", "environments", "有多少环境", "环境列表"],
    }
    for path, patterns in strong_patterns.items():
        if any(p.lower() in q for p in patterns):
            return [path]

    # Score each endpoint by its keyword list.
    scores = {}
    for ep in ADMIN_ENDPOINTS:
        score = sum(1 for kw in ep["keywords"] if kw.lower() in q)
        if score > 0:
            scores[ep["path"]] = score

    if scores:
        # If one endpoint dominates with no close runner-up, return just that one.
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_path, top_score = ranked[0]
        second_score = ranked[1][1] if len(ranked) > 1 else 0
        if top_score >= 2 and second_score == 0:
            return [top_path]

        # If the question is about clusters, keep it focused on /clusters and skip
        # loosely-matched endpoints like /environments from generic words such as "环境".
        cluster_paths = {"/clusters"}
        if cluster_paths.intersection(scores):
            cluster_score = scores.get("/clusters", 0)
            non_cluster_scores = {p: s for p, s in scores.items() if p not in cluster_paths}
            if non_cluster_scores and cluster_score >= max(non_cluster_scores.values()):
                return ["/clusters"]

        return [p for p, _ in ranked]

    # Nothing specific matched: use the default endpoints.
    return [ep["path"] for ep in ADMIN_ENDPOINTS if ep.get("default")]


def extract_json(text: str):
    """Try to extract the first JSON array/object from an LLM response."""
    text = text.strip()
    # If wrapped in markdown fences, unwrap it.
    if text.startswith("```"):
        lines = text.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    # Find the first '[' or '{' block.
    for start_char, end_char in (("[", "]"), ("{", "}")):
        start = text.find(start_char)
        if start != -1:
            depth = 0
            for i in range(start, len(text)):
                if text[i] == start_char:
                    depth += 1
                elif text[i] == end_char:
                    depth -= 1
                    if depth == 0:
                        try:
                            return json.loads(text[start : i + 1])
                        except json.JSONDecodeError:
                            break
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def select_apis_by_llm(query: str, overview_text: str, overrides: dict, env: str = "dev"):
    """Ask the LLM to pick relevant Admin API calls based on the human-readable overview."""
    if not overview_text:
        return []

    api_key = overrides.get("llmApiKey") or ENV.get("LLM_API_KEY") or ENV.get("DEEPSEEK_API_KEY") or ENV.get("KIMI_API_KEY", "")
    model = overrides.get("llmModel") or ENV.get("LLM_MODEL") or KIMI_MODEL
    base = resolve_llm_base(model, overrides.get("llmBase", ""))
    if not api_key:
        return []

    # All paths listed in the overview are read-only GET endpoints.
    valid_paths = set(re.findall(r"GET\s+(/admin/v1/[^\s`|]+)", overview_text))

    system_prompt = """You are an API planner for the ApeCloud Admin API.
You are given a markdown overview that lists all read-only (GET) APIs.
Analyze the user's question and select the minimal set of API calls needed to answer it.

Rules:
1. Only select GET API paths listed in the overview. Do not invent paths.
2. Prefer broad list endpoints. Only use endpoints with path parameters (e.g., {orgName}, {clusterName}) if the question explicitly provides the resource name/id, or if you have already fetched that id from a previous list call.
3. If multiple related resources are needed, return multiple API calls in the order they should be executed.
4. Only include queryParams when the value is clearly provided or inferable from the question. Otherwise omit queryParams.
5. Important: "dev" in the question refers to the deployment mode, NOT the platform environment resource name. Do NOT set envName="dev" unless the user explicitly names a platform environment such as "kb10" or "cloud-dev".
6. Return ONLY a JSON array in the following format (no markdown, no explanation):
[
  {"path": "/admin/v1/clusters", "reason": "Need cluster list for the environment"},
  {"path": "/admin/v1/organizations/{orgName}/clusters", "pathParams": {"orgName": "alal-test"}, "reason": "List clusters in a specific org"}
]
queryParams and pathParams are optional."""

    user_prompt = f"""User question: {query}
Deployment environment: {env}

Admin API Overview:
{overview_text}

Select the APIs to call."""

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.2,
        "stream": False,
    }
    result = llm_curl(api_key, base, payload)
    if "error" in result:
        print(f"API selection LLM error: {result['error']}")
        return []
    selected = extract_json(result.get("content", ""))
    if not isinstance(selected, list):
        print(f"API selection returned non-list: {selected}")
        return []
    valid = []
    for item in selected:
        if not isinstance(item, dict):
            continue
        path = item.get("path", "")
        if path not in valid_paths:
            print(f"API selection returned unknown path: {path}")
            continue
        # Avoid mistaking the deployment mode for a platform environment name.
        query_params = item.get("queryParams") or {}
        if query_params.get("envName") == env:
            query_params.pop("envName", None)
            if not query_params:
                item.pop("queryParams", None)
        valid.append(item)
    return valid


def execute_api_workflow(selected_apis: list, base: str, username: str, password: str):
    """Execute the selected API calls and collect their results."""
    results = {}
    for item in selected_apis:
        path = item.get("path", "")
        if not path.startswith("/admin/v1"):
            results[path] = {"error": "Invalid API path"}
            continue

        # Fill path parameters if provided.
        try:
            rendered = path.format(**(item.get("pathParams") or {}))
        except KeyError as e:
            results[path] = {"error": f"Missing path parameter {e} for {path}"}
            continue

        # Build the final URL, avoiding double /admin/v1 prefix.
        base_url = base.rstrip("/")
        if rendered.startswith("/admin/v1") and base_url.endswith("/admin/v1"):
            rendered = rendered[len("/admin/v1"):]
        url = base_url + rendered

        query_params = item.get("queryParams") or {}
        if query_params:
            url = url + "?" + urlencode(query_params)

        status, body = digest_curl(url, username, password)

        # If the call failed and we sent query params, retry without them.
        if status != 200 and query_params:
            url = base_url + rendered
            status, body = digest_curl(url, username, password)

        if status == 200:
            try:
                results[path] = json.loads(body)
            except json.JSONDecodeError:
                results[path] = {"raw": body}
        else:
            results[path] = {"error": f"HTTP {status}: {body[:200]}"}
    return results


# ─── Read-only safety guard ───
_MUTATION_VERBS = [
    "create", "delete", "update", "patch", "put", "post",
    "restart", "stop", "start", "enable", "disable", "restore",
    "rebuild", "upgrade", "scale", "expand", "promote", "expose",
    "lock", "unlock", "kill",
    "创建", "删除", "更新", "修改", "新增", "添加", "重启", "停止",
    "启动", "开启", "关闭", "恢复", "重建", "升级", "扩容", "缩容",
    "锁定", "解锁", "杀掉",
]

_INFO_MARKERS = [
    # knowledge-seeking phrases
    "如何", "怎么", "怎样", "what is", "how to", "how do",
    "介绍", "说明", "什么是", "explain", "文档",
    # question words / particles that turn a verb into a fact query
    "谁", "什么", "什么时候", "哪里", "为什么", "是否", "多少", "几个",
    "who", "what", "when", "where", "why", "whether", "how many", "how much",
    "吗", "？", "?", "呢", "呀",
]


def is_mutation_query(query: str) -> bool:
    """Detect whether the user is asking to perform a mutating admin operation."""
    q = query.lower()
    has_verb = any(kw in q for kw in _MUTATION_VERBS)
    is_info = any(m.lower() in q for m in _INFO_MARKERS)
    return has_verb and not is_info


def fetch_dev_admin_data(query: str, overrides=None):
    overrides = overrides or {}
    base = (overrides.get("adminBase") or ENV.get("ADMIN_DEV_API_BASE") or DEV_API_BASE).rstrip("/")
    username = overrides.get("adminAccessKey") or ENV.get("ADMIN_DEV_ACCESS_KEY", "")
    password = overrides.get("adminSecretKey") or ENV.get("ADMIN_DEV_SECRET_KEY", "")
    if not username or not password:
        raise RuntimeError("ADMIN_DEV_ACCESS_KEY / ADMIN_DEV_SECRET_KEY 未配置")

    paths = select_endpoints(query)
    results = {}
    for path in paths:
        status, body = digest_curl(f"{base}{path}", username, password)
        if status == 200:
            try:
                results[path] = json.loads(body)
            except json.JSONDecodeError:
                results[path] = {"raw": body}
        else:
            results[path] = {"error": f"{status}: {body[:200]}"}
    return results


# ─── LLM API (OpenAI-compatible: Kimi / DeepSeek) ───
def call_llm(query: str, env: str, admin_data=None, overrides=None):
    overrides = overrides or {}
    api_key = overrides.get("llmApiKey") or ENV.get("LLM_API_KEY") or ENV.get("DEEPSEEK_API_KEY") or ENV.get("KIMI_API_KEY", "")
    model = overrides.get("llmModel") or ENV.get("LLM_MODEL") or KIMI_MODEL
    base = resolve_llm_base(model, overrides.get("llmBase", ""))
    if not api_key:
        return {"error": "LLM API Key 未配置"}

    system_prompt = """你是 Chat2KB，一个面向 KubeBlocks 生态的对话式数据库智能助手。

你的能力：
1. 知识库问答：回答 KubeBlocks、MySQL、PostgreSQL、Redis 等数据库相关的产品文档、最佳实践、故障排查问题。
2. 运营洞察：当用户询问 dev / apecloud.cn / kubeblocks.io 等 Demo 环境的数据时，基于提供的实时数据给出简洁、结构化的分析。

回答要求：
- 用中文回答。
- 给出结论前先列出关键数据点，并以可视化方式展示（表格、列表、加粗指标等）。
- 涉及对比、排名、利用率时使用列表或表格形式。
- 如果提供了 API 原始数据，基于这些数据推理，不要编造。
- 如果未提供实时 API 数据（通用知识库问题），请在每条关键信息后用 `[来源：...]` 标注来源，可选值包括 `KubeBlocks 官方文档`、`MySQL 官方文档`、`PostgreSQL 官方文档`、`Redis 官方文档`、`社区最佳实践` 等，以便用户验证依据。
- 如果数据不足，明确说明并给出建议。"""

    admin_ok = admin_data and any(not isinstance(v, dict) or not v.get("error") for v in admin_data.values())
    if admin_ok:
        system_prompt += f"\n\n[dev 环境实时数据]\n{json.dumps(admin_data, ensure_ascii=False, indent=2)}\n\n请基于以上数据回答用户关于 dev 环境的问题。"
    elif env == "dev":
        system_prompt += "\n\n注意：当前 dev 环境的实时数据接口未配置或暂时不可用，请基于你的知识回答，并提示用户检查 ADMIN_DEV_ACCESS_KEY / ADMIN_DEV_SECRET_KEY。"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        "temperature": 1,
        "stream": False,
    }

    result = llm_curl(api_key, base, payload)
    if "error" in result:
        return result
    result["env"] = env
    result["source"] = "llm+admin-dev" if admin_ok else "llm"
    if admin_ok:
        result["adminData"] = admin_data
    return result


# ─── HTTP Handler ───
class Chat2KBHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        # quieter logs
        print(f"[{self.date_time_string()}] {fmt % args}")

    def _send_json(self, status: int, obj: dict):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        return json.loads(body)

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _handle_save_settings(self):
        try:
            data = self._read_json_body()
            save_settings(data)
            self._send_json(200, {"ok": True, "settings": get_settings()})
        except Exception as e:
            self._send_json(500, {"error": f"保存设置失败: {e}"})

    def _handle_test_admin(self):
        try:
            data = self._read_json_body()
            base = data.get("adminBase", "").strip()
            username = data.get("adminAccessKey", "").strip()
            password = data.get("adminSecretKey", "").strip()
            if not base or not username or not password:
                return self._send_json(400, {"ok": False, "error": "请填写 Admin API Base URL、Access Key 和 Secret Key"})
            ok, err = test_admin_connection(base, username, password)
            self._send_json(200, {"ok": ok, "error": err})
        except Exception as e:
            self._send_json(500, {"ok": False, "error": f"测试失败: {e}"})

    def _handle_test_llm(self):
        try:
            data = self._read_json_body()
            api_key = data.get("llmApiKey", "").strip()
            model = data.get("llmModel", "").strip()
            base = data.get("llmBase", "").strip()
            if not api_key:
                return self._send_json(400, {"ok": False, "error": "请填写 API Key"})
            ok, err = test_llm_connection(api_key, model, base)
            self._send_json(200, {"ok": ok, "error": err})
        except Exception as e:
            self._send_json(500, {"ok": False, "error": f"测试失败: {e}"})

    def _handle_chat(self):
        try:
            data = self._read_json_body()
            user_env = data.get("env", "general")
            query = data.get("query", "")

            # Start with persisted settings, then allow request body to override
            overrides = get_settings()
            for k in (
                "adminBase", "adminAccessKey", "adminSecretKey",
                "llmApiKey", "llmModel", "llmApiId", "llmBase",
            ):
                if data.get(k):
                    overrides[k] = data[k]

            # ─── Read-only guard for non-general environments ───
            if user_env != "general" and is_mutation_query(query):
                self._send_json(200, {
                    "content": "⚠️ 当前环境只支持只读查询，无法执行创建、修改、删除等操作。如需执行此类操作，请通过控制台进行。",
                    "env": user_env,
                    "source": "readonly-guard",
                })
                return

            admin_data = None
            if user_env != "general":
                try:
                    base = (overrides.get("adminBase") or ENV.get("ADMIN_DEV_API_BASE") or DEV_API_BASE).rstrip("/")
                    username = overrides.get("adminAccessKey") or ENV.get("ADMIN_DEV_ACCESS_KEY", "")
                    password = overrides.get("adminSecretKey") or ENV.get("ADMIN_DEV_SECRET_KEY", "")
                    if username and password:
                        # Use the human-readable admin API overview to plan the
                        # read-only workflow. Fall back to keyword selection if the
                        # overview is missing or the planner returns nothing.
                        if ADMINAPI_OVERVIEW:
                            selected = select_apis_by_llm(query, ADMINAPI_OVERVIEW, overrides, env=user_env)
                            if selected:
                                admin_data = execute_api_workflow(selected, base, username, password)
                            else:
                                admin_data = fetch_dev_admin_data(query, overrides)
                        else:
                            admin_data = fetch_dev_admin_data(query, overrides)
                except Exception as e:
                    print(f"admin workflow error: {e}")

            result = call_llm(query, user_env, admin_data, overrides)
            # If Kimi itself returns an error dict, wrap it as a user-facing content
            # so the UI still shows the dev admin data when available.
            if "error" in result:
                if admin_data and any(not isinstance(v, dict) or not v.get("error") for v in admin_data.values()):
                    result = {
                        "content": f"⚠️ 后端 AI 服务异常：{result['error']}\n\n已获取到的 dev 实时数据如下，供参考：\n\n```json\n{json.dumps(admin_data, ensure_ascii=False, indent=2)}\n```",
                        "env": user_env,
                        "source": "admin-dev-only",
                        "adminData": admin_data,
                    }

            if user_env == "general" and "error" not in result:
                result["content"] += "\n\n---\n**参考来源**：本回答基于大语言模型的通用知识及 KubeBlocks、MySQL、PostgreSQL、Redis 等官方文档与社区最佳实践整理生成，具体实现请以对应官方文档为准。"

            self._send_json(200, result)
        except Exception as e:
            self._send_json(500, {"error": f"服务器内部错误: {e}"})

    def do_OPTIONS(self):
        if self.path in ("/api/chat", "/api/settings", "/api/test/admin", "/api/test/llm"):
            self.send_response(204)
            self._cors_headers()
            self.end_headers()
        else:
            self.send_response(405)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/chat":
            return self._handle_chat()
        if self.path == "/api/settings":
            return self._handle_save_settings()
        if self.path == "/api/test/admin":
            return self._handle_test_admin()
        if self.path == "/api/test/llm":
            return self._handle_test_llm()
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?", 1)[0]

        if path == "/api/settings":
            try:
                self._send_json(200, get_settings())
            except Exception as e:
                self._send_json(500, {"error": f"读取设置失败: {e}"})
            return

        if path == "/":
            path = "/index.html"
        file_path = Path(__file__).parent / path.lstrip("/")

        # prevent directory traversal
        root = Path(__file__).parent.resolve()
        try:
            file_path.resolve().relative_to(root)
        except ValueError:
            self.send_response(403)
            self.end_headers()
            return

        if not file_path.exists() or file_path.is_dir():
            self.send_response(404)
            self.end_headers()
            return

        content_type = "text/plain"
        if path.endswith(".html"):
            content_type = "text/html; charset=utf-8"
        elif path.endswith(".css"):
            content_type = "text/css; charset=utf-8"
        elif path.endswith(".js"):
            content_type = "application/javascript; charset=utf-8"
        elif path.endswith(".svg"):
            content_type = "image/svg+xml"

        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    parser = argparse.ArgumentParser(description="Chat2KB local dev server")
    parser.add_argument("port", nargs="?", type=int, default=DEFAULT_PORT, help="port to listen on")
    args = parser.parse_args()

    init_db()
    server = HTTPServer(("", args.port), Chat2KBHandler)
    print(f"Chat2KB server running at http://localhost:{args.port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
