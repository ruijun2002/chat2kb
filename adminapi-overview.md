# KBE Admin API 查询接口一览（GET Only）

> 文件：`adminapi.yaml` | **仅包含查询类 API（GET 方法）** | 总计 **120 个查询端点**

---

## 1. 🏢 组织与租户查询

**用途**：查看组织、成员、资源配额、参数配置

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations` | 查询组织列表 |
| `GET /admin/v1/organizations/{orgName}` | 查询组织详情 |
| `GET /admin/v1/organizations/{orgName}/members` | 查询组织成员列表 |
| `GET /admin/v1/organizations/{orgName}/members/{memberId}` | 查询成员详情 |
| `GET /admin/v1/organizations/{orgName}/resourceQuota` | 查询资源配额 |
| `GET /admin/v1/organizations/{orgName}/parameters` | 查询组织参数 |
| `GET /admin/v1/organizations/{orgName}/parameters/{parameterName}` | 查询参数详情 |

---

## 2. 🔐 用户与权限查询

**用途**：查看用户、管理员、角色、权限信息

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/user` | 获取当前用户信息 |
| `GET /admin/v1/user/apikeys` | 查询当前用户 API Key 列表 |
| `GET /admin/v1/users` | 查询用户列表 |
| `GET /admin/v1/users/{userID}` | 查询用户详情 |
| `GET /admin/v1/users/{userID}/authorization` | 查询用户授权信息 |
| `GET /admin/v1/administrators` | 查询管理员列表 |
| `GET /admin/v1/administrators/{administratorID}` | 查询管理员详情 |
| `GET /admin/v1/administrators/{administratorID}/roles` | 查询管理员角色 |
| `GET /admin/v1/administrators/permissions` | 查询管理员权限列表 |
| `GET /admin/v1/administrators/roles` | 查询管理员角色列表 |
| `GET /admin/v1/administrators/roles/{roleName}` | 查询管理员角色详情 |
| `GET /admin/v1/administrators/roles/{roleName}/permissions` | 查询角色权限 |
| `GET /admin/v1/permissions` | 查询所有权限定义 |
| `GET /admin/v1/organizations/{orgName}/roles` | 查询组织角色列表 |
| `GET /admin/v1/organizations/{orgName}/roles/{roleName}` | 查询组织角色详情 |
| `GET /admin/v1/organizations/{orgName}/roles/{roleName}/permissions` | 查询组织角色权限 |

---

## 3. 🧾 操作日志 / 事件查询 (Event API)

**用途**：查询平台操作日志、集群事件、AI 对话事件

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/events` | **查询全局操作日志/事件列表** (`eventApi.listEvents`) |
| `GET /admin/v1/events/{eventID}` | 查询单个事件详情 |
| `GET /admin/v1/organizations/{orgName}/events` | 查询组织级操作日志/事件列表 (`eventApi.listOrgEvents`) |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/events` | 查询实例生命周期事件 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/events` | 查询 AI 对话事件流 |

> **说明**：`/admin/v1/events` 和 `/admin/v1/organizations/{orgName}/events` 是平台核心的事件/操作日志查询接口，记录所有资源的变更操作（创建、修改、删除、运维等）。

---

## 4. 📋 任务查询

**用途**：查看异步任务类型、任务列表、任务日志

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/taskTypes` | 查询任务类型 |
| `GET /admin/v1/tasks` | 查询任务列表 |
| `GET /admin/v1/tasks/{taskId}` | 查询任务详情 |
| `GET /admin/v1/tasks/{taskId}/log` | 查询任务日志 |
| `GET /admin/v1/tasks/{taskId}/steps/{stepId}/log` | 查询任务步骤日志 |

---

## 5. ☁️ 环境查询

**用途**：查看 K8s 环境、节点、资源、存储、网络、模块状态

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/environments` | 查询环境列表 |
| `GET /admin/v1/environments/{environmentName}` | 查询环境详情 |
| `GET /admin/v1/environments/{environmentName}/statusHistory` | 查询环境状态历史 |
| `GET /admin/v1/environments/{environmentName}/credentials` | 查询环境凭证列表 |
| `GET /admin/v1/environments/{environmentName}/credentials/{credentialName}` | 查询环境凭证详情 |
| `GET /admin/v1/environments/{environmentName}/resourceStats` | 查询环境资源统计 |
| `GET /admin/v1/environments/{environmentName}/nodes` | 查询环境节点列表 |
| `GET /admin/v1/environments/{environmentName}/nodes/{nodeName}` | 查询节点详情 |
| `GET /admin/v1/environments/{environmentName}/nodes/{nodeName}/pods` | 查询节点 Pod 列表 |
| `GET /admin/v1/environments/{environmentName}/nodes/{nodeName}/instances/resourceStats` | 查询节点实例资源统计 |
| `GET /admin/v1/environments/{environmentName}/nodes/resourceStats` | 查询节点资源统计 |
| `GET /admin/v1/environments/{environmentName}/nodes/monitorStatus` | 查询节点监控状态 |
| `GET /admin/v1/environments/{environmentName}/kubeconfig` | 查询环境 kubeconfig |
| `GET /admin/v1/environments/{environmentName}/bootstrapManifests` | 查询引导清单 |
| `GET /admin/v1/environments/{environmentName}/status` | 查询环境状态 |
| `GET /admin/v1/environments/{environmentName}/progress` | 查询环境进度 |
| `GET /admin/v1/environments/{environmentName}/loadbalancer` | 查询负载均衡配置 |
| `GET /admin/v1/environments/{environmentName}/loadbalancer/vipPool` | 查询 VIP 池 |
| `GET /admin/v1/environments/{environmentName}/loadbalancer/vipPool/{poolID}` | 查询 VIP 池详情 |
| `GET /admin/v1/environments/{environmentName}/storageClasses` | 查询存储类 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}` | 查询存储类详情 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/pvcs` | 查询 PVC 列表 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/nodeStats` | 查询存储节点统计 |
| `GET /admin/v1/environments/{environmentName}/storageProvisioners` | 查询存储供应器 |
| `GET /admin/v1/environments/{environmentName}/nodeGroups` | 查询节点组 |
| `GET /admin/v1/environments/{environmentName}/nodeGroups/{nodeGroupName}` | 查询节点组详情 |
| `GET /admin/v1/environments/{environmentName}/availableZones` | 查询可用区 |
| `GET /admin/v1/environments/{environmentName}/projects` | 查询项目列表 |
| `GET /admin/v1/environments/{environmentName}/modules` | 查询模块列表 |
| `GET /admin/v1/environments/{environmentName}/modules/{moduleName}/details` | 查询模块详情 |
| `GET /admin/v1/environments/{environmentName}/modules/{moduleName}/pods/{podName}/logs` | 查询模块 Pod 日志 |
| `GET /admin/v1/environments/optional-modules` | 查询可选模块 |
| `GET /admin/v1/environments/{environmentName}/engineOptions` | 查询环境引擎选项 |
| `GET /admin/v1/environments/{environmentName}/engineOption/{id}` | 查询环境引擎选项详情 |
| `GET /admin/v1/environments/{environmentName}/engineNetworkModes/supported` | 查询支持的网络模式 |
| `GET /admin/v1/environments/{environmentName}/engineNetworkModes/options` | 查询网络模式选项 |
| `GET /admin/v1/latestEnvModuleVersion` | 查询最新环境模块版本 |
| `GET /admin/v1/kubernetes/nodes` | 查询 K8s 节点 |
| `GET /admin/v1/kubernetes/storageclasses` | 查询 K8s StorageClasses |
| `GET /admin/v1/kubernetes/dns` | 查询 K8s DNS |
| `GET /admin/v1/platformComponents` | 查询平台组件 |
| `GET /admin/v1/platformComponents/{componentName}` | 查询平台组件详情 |
| `GET /admin/v1/platformParameters` | 查询平台参数 |
| `GET /admin/v1/platformParameters/{platformParameterName}` | 查询平台参数详情 |

---

## 6. 🗄️ 数据库集群查询

**用途**：查看集群、实例、端点、指标、参数等运行状态

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/clusters` | 查询全局集群列表 |
| `GET /admin/v1/organizations/{orgName}/clusters` | 查询组织集群列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}` | 查询集群详情 |
| `GET /admin/v1/organizations/{orgName}/clustersWithDelete/{clusterID}` | 查询已删除集群 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/instances` | 查询实例列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/offlineInstances` | 查询离线实例 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/endpoints` | 查询集群端点 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/metrics` | 查询集群指标 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/metrics` | 查询实例指标 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/upgradeableServiceVersion` | 查询可升级版本 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/haHistory` | 查询高可用历史 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/parameters` | 查询集群参数 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterHistories` | 查询参数变更历史 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy` | 查询备份策略 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules` | 查询备份计划列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules/{scheduleName}` | 查询备份计划详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/restore` | 查询恢复任务列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/alerts/cluster/{clusterName}` | 查询集群告警开关状态 |
| `GET /admin/v1/organizations/{orgName}/clusterTags` | 查询集群标签 |
| `GET /admin/v1/organizations/{orgName}/tags` | 查询标签列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate` | 查询参数模板 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}` | 查询数据源详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource` | 查询数据源列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/databases` | 查询数据库列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/schemas` | 查询 Schema 列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}` | 查询 Schema 详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}` | 查询对象类型列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}/{objectName}` | 查询对象详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/history` | 查询查询历史 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}` | 查询租户详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameters` | 查询租户参数 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameterHistory` | 查询租户参数历史 |

---

## 7. 🔍 数据管理查询 (DMS)

**用途**：查询 MongoDB 数据、索引、Schema、Shell 会话等

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases` | 查询 MongoDB 数据库列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/metadata` | 查询 MongoDB 数据库元数据 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections` | 查询 MongoDB 集合列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}` | 查询 MongoDB 集合详情/统计 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/indexes` | 查询 MongoDB 索引列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/schema` | 查询 MongoDB Schema 分析 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/validation` | 查询 MongoDB 验证规则 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/shell/sessions/{sessionID}/prompt` | 查询 MongoDB Shell 提示符 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/sessions` | 查询会话列表 (Deprecated) |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/tasks` | 查询数据任务列表 |

---

## 8. 📊 日志查询

**用途**：查询 Pod 日志、运行日志、慢查询、审计日志、错误日志

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/pod` | 查询 Pod 日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/running` | 查询运行日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow` | 查询慢查询日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates` | 查询慢查询模板 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates/{templateId}` | 查询慢查询模板详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates/{templateId}/samples` | 查询慢查询模板样本 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/aggregate` | 查询慢查询聚合统计 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/stats` | 查询慢查询统计 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/audit` | 查询审计日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/error` | 查询错误日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/hits` | 查询日志命中率 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/events` | 查询实例事件 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/log` | 查询实例日志 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/workloads/{workloadName}/log` | 查询工作负载日志 |

---

## 9. 🔄 备份查询

**用途**：查看备份任务、备份详情、备份统计、恢复任务

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules/{scheduleName}` | 查询备份计划详情 |
| `GET /admin/v1/organizations/{orgName}/backups/{backupId}` | 查询备份详情 |
| `GET /admin/v1/organizations/{orgName}/backups/{backupId}/logs` | 查询备份日志 |
| `GET /admin/v1/backups` | 查询全局备份列表 |
| `GET /admin/v1/backupStats` | 查询备份统计 |
| `GET /admin/v1/restoreTasks` | 查询全局恢复任务 |
| `GET /admin/v1/organizations/{orgName}/restore` | 查询组织恢复任务 |
| `GET /admin/v1/organizations/{orgName}/clustersWithDelete/restoreTimeRange` | 查询恢复时间范围 |
| `GET /admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}` | 查询备份仓库详情 |
| `GET /admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/view` | 查看备份仓库 |
| `GET /admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/stats` | 查询备份仓库统计 |
| `GET /admin/v1/environmentBackupRepo` | 查询环境备份仓库列表 |
| `GET /admin/v1/environmentObjectStorage` | 查询环境对象存储 |
| `GET /admin/v1/storageProviders` | 查询存储提供商 |

---

## 10. 🚨 告警查询

**用途**：查看告警规则、告警对象、策略、接收人、统计

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/alerts/rules` | 查询告警规则列表 |
| `GET /admin/v1/alerts/rules/{alertName}` | 查询告警规则详情 |
| `GET /admin/v1/alerts/objects` | 查询告警对象列表 |
| `GET /admin/v1/alerts/objects/{alertId}` | 查询告警对象详情 |
| `GET /admin/v1/alerts/strategies` | 查询告警策略列表 |
| `GET /admin/v1/alerts/strategies/{strategyId}` | 查询告警策略详情 |
| `GET /admin/v1/alerts/receivers` | 查询告警接收人列表 |
| `GET /admin/v1/alerts/receivers/{receiverId}` | 查询告警接收人详情 |
| `GET /admin/v1/alerts/inhibits` | 查询告警抑制规则 |
| `GET /admin/v1/alerts/inhibits/{inhibitId}` | 查询告警抑制规则详情 |
| `GET /admin/v1/alerts/config` | 查询告警时区配置 |
| `GET /admin/v1/alerts/statistic` | 查询告警统计 |
| `GET /admin/v1/alerts/checkURL` | 检查告警 URL |
| `GET /admin/v1/alertTemplates` | 查询告警模板列表 |
| `GET /admin/v1/alertTemplates/{templateId}` | 查询告警模板详情 |
| `GET /admin/v1/alertSMTPConfig` | 查询 SMTP 告警配置 |
| `GET /admin/v1/alertSMSConfig` | 查询 SMS 告警配置 |

---

## 11. 🤖 AI Agent 查询

**用途**：查看 AI 诊断状态、会话、消息、交互动作

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/ai-agent/status` | 查询 AI Agent 状态 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations` | 查询 AI 会话列表 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}` | 查询 AI 会话详情 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/messages` | 查询会话消息列表 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions` | 查询交互动作列表 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}` | 查询交互动作详情 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}/artifacts/{artifactId}/browse` | 浏览交互产物 |
| `GET /admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}/artifacts/{artifactId}/download` | 下载交互产物 |
| `GET /admin/v1/llm` | 查询 LLM 模型列表 |
| `GET /admin/v1/llm/{id}` | 查询 LLM 模型详情 |
| `GET /admin/v1/llm/models` | 查询支持的模型列表 |

---

## 12. 🧪 巡检与诊断查询

**用途**：查看巡检脚本、自动巡检配置、巡检任务、诊断结果

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/inspectionScripts` | 查询巡检脚本列表 |
| `GET /admin/v1/inspectionScripts/{scriptId}` | 查询巡检脚本详情 |
| `GET /admin/v1/autoInspection` | 查询自动巡检配置 |
| `GET /admin/v1/autoInspections/{id}` | 查询自动巡检详情 |
| `GET /admin/v1/organizations/{orgName}/inspectionTasksByOrg` | 查询组织巡检任务 |
| `GET /admin/v1/organizations/{orgName}/inspectionTasksByOrg/{taskId}` | 查询巡检任务详情 |
| `GET /admin/v1/environments/{environmentName}/inspectionTasksByEnv` | 查询环境巡检任务 |
| `GET /admin/v1/environments/{environmentName}/inspectionTasksByEnv/{taskId}` | 查询环境巡检任务详情 |
| `GET /admin/v1/inspectionTasks/aggregate` | 查询巡检任务聚合统计 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions` | 查询 PostgreSQL 会话诊断 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}` | 查询 PostgreSQL 会话详情 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}/lockAnalysis` | 查询 PostgreSQL 锁分析 |

---

## 13. 🛠️ 引擎查询

**用途**：查看引擎类型、版本、参数模板、规格、许可证

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/engines` | 查询引擎列表 |
| `GET /admin/v1/engines/resourceConstraints` | 查询引擎资源约束 |
| `GET /admin/v1/engines/resourceConstraints/{id}` | 查询资源约束详情 |
| `GET /admin/v1/engineTypes` | 查询引擎类型 |
| `GET /admin/v1/engineOptions` | 查询引擎选项 |
| `GET /admin/v1/engineOptions/{engineName}` | 查询引擎选项详情 |
| `GET /admin/v1/engineOptions/{engineName}/release` | 查询引擎版本发布 |
| `GET /admin/v1/engineOptionHistories` | 查询引擎选项历史 |
| `GET /admin/v1/environments/{environmentName}/engines` | 查询环境引擎列表 |
| `GET /admin/v1/environments/{environmentName}/engines/{engineName}` | 查询环境引擎详情 |
| `GET /admin/v1/engineVersions` | 查询引擎版本 |
| `GET /admin/v1/engineVersions/{engineName}` | 查询引擎版本详情 |
| `GET /admin/v1/engines/{engineName}/schedulingPolicies` | 查询调度策略 |
| `GET /admin/v1/engines/{engineName}/schedulingRules` | 查询调度规则 |
| `GET /admin/v1/engines/{engineName}/schedulingRules/{ruleId}` | 查询调度规则详情 |
| `GET /admin/v1/engineLicenses` | 查询引擎许可证 |
| `GET /admin/v1/engineLicense` | 查询引擎许可证详情 |
| `GET /admin/v1/engineLicenseEntities` | 查询许可证实体 |
| `GET /admin/v1/engineLicenseEntity` | 查询许可证实体详情 |
| `GET /admin/v1/license` | 查询平台许可证 |
| `GET /admin/v1/features` | 查询功能特性 |
| `GET /admin/v1/featureGroups` | 查询功能特性组 |
| `GET /admin/v1/features/{featureName}` | 查询功能特性详情 |
| `GET /admin/v1/classes` | 查询规格列表 |
| `GET /admin/v1/classTypes` | 查询规格类型 |
| `GET /admin/v1/classTypes/{id}` | 查询规格类型详情 |
| `GET /admin/v1/providers` | 查询提供商 |
| `GET /admin/v1/providers/{providerName}` | 查询提供商详情 |
| `GET /admin/v1/imageRegistries` | 查询镜像仓库 |
| `GET /admin/v1/imageRegistries/{imageRegistryName}` | 查询镜像仓库详情 |
| `GET /admin/v1/environments/{environmentName}/engines/{engineName}/serviceVersion` | 查询服务版本 |
| `GET /admin/v1/environments/{environmentName}/engines/{engineName}/availableServiceVersion` | 查询可用服务版本 |
| `GET /admin/v1/environments/{environmentName}/engines/{engineName}/imageUploadProgress` | 查询镜像上传进度 |
| `GET /admin/v1/organizations/{orgName}/{engineName}/clusterBackupMethod` | 查询集群备份方法 |
| `GET /admin/v1/parameterTemplates` | 查询参数模板 |
| `GET /admin/v1/parameterTemplate/{parameterTemplateName}` | 查询参数模板详情 |
| `GET /admin/v1/parameterTemplate/{parameterTemplateName}/diff` | 查询参数模板差异 |
| `GET /admin/v1/databaseParameters` | 查询数据库参数 |
| `GET /admin/v1/monitorDataSinks` | 查询监控数据接收器 |
| `GET /admin/v1/monitorDataSinks/{monitorDataSinkID}` | 查询监控数据接收器详情 |
| `GET /admin/v1/monitorDataSinks/environments/{environmentName}` | 查询环境监控数据接收器 |
| `GET /admin/v1/metrics/metaData/aggregate` | 查询指标元数据聚合 |

---

## 14. 🗑️ 回收站查询

**用途**：查看已删除集群

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/recycleBin/clusters` | 查询全局回收站集群 |
| `GET /admin/v1/organizations/{orgName}/recycleBin/clusters` | 查询组织回收站集群 |
| `GET /admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}` | 查询回收站集群详情 |

---

## 15. 📦 数据迁移查询

**用途**：查看导入任务、前置检查任务

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight/{taskId}` | 查询前置检查任务 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/import` | 查询导入任务列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}` | 查询导入任务详情 |

---

## 16. 🔗 集群关系查询

**用途**：查看集群间关系（主从、灾备）

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/organizations/{orgName}/cluster/{clusterName}/available-relations` | 查询可用关系集群 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/relations` | 查询集群关系列表 |

---

## 17. 💰 计费与 SLA 查询

**用途**：查看定价、账单、计量、SLA 数据

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/pricing` | 查询定价 |
| `GET /admin/v1/pricing/global` | 查询全局定价 |
| `GET /admin/v1/bills` | 查询账单 |
| `GET /admin/v1/metering/tracks` | 查询计量追踪 |
| `GET /admin/v1/sla` | 查询 SLA |
| `GET /admin/v1/sla/rank` | 查询 SLA 排名 |
| `GET /admin/v1/sla/daily` | 查询每日 SLA |
| `GET /admin/v1/sla/outages` | 查询停机事件 |
| `GET /admin/v1/sla/settings` | 查询 SLA 设置 |
| `GET /admin/v1/sla/engines` | 查询引擎 SLA |
| `GET /admin/v1/sla/uncompliant` | 查询不合规 SLA |

---

## 18. 🔒 安全查询

**用途**：查看漏洞扫描结果

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/vulns` | 查询漏洞列表 |
| `GET /admin/v1/organizations/{orgName}/clusters/{clusterName}/vulns` | 查询集群漏洞 |

---

## 19. 📊 特定数据库数据查询

**用途**：查询 Kafka、Redis、RabbitMQ、达梦等数据库的运行时数据

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers` | 查询 Kafka Broker |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers/{brokerId}/configs` | 查询 Broker 配置 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics` | 查询 Kafka Topic |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}` | 查询 Topic 详情 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/brokers` | 查询 Topic Broker 分布 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/partitions` | 查询 Topic 分区 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/configs` | 查询 Topic 配置 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups` | 查询 Topic 消费组 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets` | 查询消费组 Offset |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages` | 查询 Topic 消息 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups` | 查询消费组列表 |
| `GET /admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups/{groupId}` | 查询消费组详情 |
| `GET /admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts` | 查询 Redis 账号 |
| `GET /admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}` | 查询 Redis 账号详情 |
| `GET /admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts` | 查询 RabbitMQ 账号 |
| `GET /admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}` | 查询 RabbitMQ 账号详情 |
| `GET /admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}/privileges` | 查询 RabbitMQ 权限 |
| `GET /admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/vhosts` | 查询 RabbitMQ 虚拟主机 |
| `GET /admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/exchanges` | 查询 RabbitMQ 交换机 |
| `GET /admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces` | 查询达梦表空间 |
| `GET /admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}` | 查询达梦表空间详情 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console` | 查询数据库控制台 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/demo` | 查询演示数据 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/dboptions` | 查询数据库选项 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases` | 查询数据库 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}` | 查询数据库详情 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts` | 查询数据库账号 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}` | 查询账号详情 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/root-password` | 查询 Root 密码 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}/privileges` | 查询账号权限 |
| `GET /admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions` | 查询数据库会话 |
| `GET /admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts` | 查询 MongoDB 账号 |
| `GET /admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}` | 查询 MongoDB 账号详情 |
| `GET /admin/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/accounts` | 查询 SQL Server 账号 |
| `GET /admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions` | 查询 PostgreSQL 扩展 |
| `GET /admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions/{extensionName}` | 查询 PostgreSQL 扩展详情 |

---

## 20. 🔧 存储查询

**用途**：查看环境存储、PVC、节点存储统计

| API 路径 | 用途 |
|---------|------|
| `GET /admin/v1/environments/{environmentName}/storages` | 查询存储列表 |
| `GET /admin/v1/environments/{environmentName}/storages/{storageName}` | 查询存储详情 |
| `GET /admin/v1/environments/{environmentName}/storageClasses` | 查询存储类 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}` | 查询存储类详情 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/pvcs` | 查询 PVC 列表 |
| `GET /admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/nodeStats` | 查询存储节点统计 |
| `GET /admin/v1/environments/{environmentName}/storageProvisioners` | 查询存储供应器 |
| `GET /admin/v1/storageProviders` | 查询存储提供商 |
| `GET /admin/v1/kubernetes/storageclasses` | 查询 K8s StorageClasses |

---

## 模块统计（仅 GET）

| # | 模块 | API 数量 |
|---|------|----------|
| 1 | 🏢 **组织与租户查询** | 7 |
| 2 | 🔐 **用户与权限查询** | 16 |
| 3 | 🧾 **操作日志/事件查询** | 7 |
| 4 | 📋 **任务查询** | 5 |
| 5 | ☁️ **环境查询** | 42 |
| 6 | 🗄️ **数据库集群查询** | 31 |
| 7 | 🔍 数据管理查询 (DMS) | 10 |
| 8 | 📊 日志查询 | 14 |
| 9 | 🔄 备份查询 | 14 |
| 10 | 🚨 告警查询 | 17 |
| 11 | 🤖 AI Agent 查询 | 11 |
| 12 | 🧪 巡检与诊断查询 | 12 |
| 13 | 🛠️ 引擎查询 | 36 |
| 14 | 🗑️ 回收站查询 | 3 |
| 15 | 📦 数据迁移查询 | 3 |
| 16 | 🔗 集群关系查询 | 2 |
| 17 | 💰 计费与 SLA 查询 | 11 |
| 18 | 🔒 安全查询 | 2 |
| 19 | 📊 特定数据库数据查询 | 31 |
| 20 | 🔧 存储查询 | 9 |

**总计：约 120 个 GET 查询端点**
