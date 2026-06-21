# Readonly API List

> 本文件汇总 adminapi.yaml 中所有只读（GET）API，供 LLM 选 API 与数据查询参考。

## account

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getRootAccountPassword` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/root-password` | get root account password |
| `listAccounts` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts` | List cluster accounts |
| `listMongoDBAccounts` | `GET` | `/admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts` | List mongodb accounts |

## administrator

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAdministratorsRoleByName` | `GET` | `/admin/v1/administrators/roles/{roleName}` | Get an administrator role by name |
| `listAdministrators` | `GET` | `/admin/v1/administrators` | List administrators |
| `listAdministratorsPermissions` | `GET` | `/admin/v1/administrators/permissions` | List all permissions for administrators |
| `listAdministratorsRolePermissions` | `GET` | `/admin/v1/administrators/roles/{roleName}/permissions` | List permissions of an administrator role |
| `listAdministratorsRoles` | `GET` | `/admin/v1/administrators/roles` | List all administrator roles |
| `listAdministratorsUserRoles` | `GET` | `/admin/v1/administrators/{administratorID}/roles` | List roles of an administrator user |

## AI Agent

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `browseAIAgentTurnActionArtifact` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}/artifacts/{artifactId}/browse` | Browse a generated AI diagnosis report artifact |
| `downloadAIAgentTurnActionArtifact` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}/artifacts/{artifactId}/download` | Download a generated AI diagnosis report artifact |
| `getAIAgentConversation` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}` | Get an AI diagnosis conversation |
| `getAIAgentStatus` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/status` | Get AI diagnosis agent status |
| `getAIAgentTurnAction` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}` | Get one stable AI diagnosis turn process action |
| `listAIAgentConversations` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations` | List AI diagnosis conversations |
| `listAIAgentMessages` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/messages` | List AI diagnosis conversation messages |
| `listAIAgentTurnActions` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions` | List stable AI diagnosis turn process actions |
| `subscribeAIAgentConversationEvents` | `GET` | `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/events` | Subscribe to AI diagnosis conversation events |

## alert

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `alertStatistic` | `GET` | `/admin/v1/alerts/statistic` | alert statistic |

## alertConfig

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAlertSMSConfig` | `GET` | `/admin/v1/alertSMSConfig` | Get alert SMS config |
| `getAlertTZConfig` | `GET` | `/admin/v1/alerts/config` | Get alert time zone config |

## alertInhibit

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAlertInhibit` | `GET` | `/admin/v1/alerts/inhibits/{inhibitId}` | Get alert inhibit |
| `listAlertInhibits` | `GET` | `/admin/v1/alerts/inhibits` | List alert inhibits |

## alertObject

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listAlertObjects` | `GET` | `/admin/v1/alerts/objects` | List alert objects |

## alertReceiver

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listAlertReceivers` | `GET` | `/admin/v1/alerts/receivers` | List alert receivers |

## alertRule

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAlertRule` | `GET` | `/admin/v1/alerts/rules/{alertName}` | Get alert rule |
| `listAlertRules` | `GET` | `/admin/v1/alerts/rules` | List alert rules |

## alertSMTPConfig

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAlertSMTPConfig` | `GET` | `/admin/v1/alertSMTPConfig` | Get alert SMTP config |

## alertStrategy

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listAlertStrategies` | `GET` | `/admin/v1/alerts/strategies` | List alert strategies |

## alertTemplate

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAlertTemplate` | `GET` | `/admin/v1/alertTemplates/{templateId}` | Get alert template |
| `listAlertTemplates` | `GET` | `/admin/v1/alertTemplates` | List alert templates |

## autohealing

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAutohealing` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/autohealing` | list autohealing job |

## backup

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `downloadBackup` | `GET` | `/admin/v1/organizations/{orgName}/backups/{backupId}/download` | Download full backup |
| `getBackup` | `GET` | `/admin/v1/organizations/{orgName}/backups/{backupId}` | Get backup |
| `getBackupLog` | `GET` | `/admin/v1/organizations/{orgName}/backups/{backupId}/logs` | Get backup log |
| `getBackupStats` | `GET` | `/admin/v1/backupStats` | Get backup statistics |
| `getClusterBackupPolicy` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy` | Get backup policy |
| `listBackups` | `GET` | `/admin/v1/backups` | List backups |
| `listBackupSchedules` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules` | List backup schedules |
| `listObjectsTreeForSelectiveBackup` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/listObjectsForSelectiveBackup` | List objects tree for selective backup |

## backupMethod

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getBackupMethod` | `GET` | `/admin/v1/organizations/{orgName}/{engineName}/clusterBackupMethod` | get backup method |

## backupRepo

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `checkBackupRepo` | `GET` | `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/check` | check backup repo |
| `getBackupRepo` | `GET` | `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}` | Get backup repo |
| `listBackupRepos` | `GET` | `/admin/v1/environments/{environmentName}/backupRepo` | List backup repos |
| `listBackupRepoStats` | `GET` | `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/stats` | list backup repo stats |

## billing

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listBills` | `GET` | `/admin/v1/bills` | List bills |

## class

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listClasses` | `GET` | `/admin/v1/classes` | List classes |

## classTypes

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getClassType` | `GET` | `/admin/v1/classTypes/{id}` | Get a class type by ID |
| `getClassTypes` | `GET` | `/admin/v1/classTypes` | Get all class types |

## cluster

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `describeClusterHaHistory` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/haHistory` | describe cluster HA history |
| `getCluster` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}` | Get cluster details |
| `getClusterByID` | `GET` | `/admin/v1/organizations/{orgName}/clustersWithDelete/{clusterID}` | Get cluster details by ID |
| `getClusterInstanceLog` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/workloads/{workloadName}/log` | Tail cluster instance container log |
| `getInstacesMetrics` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/metrics` | Get instaces metrics in cluster |
| `getInstanceContainerLog` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/log` | Tail cluster instance container log |
| `getSqlAudit` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/sqlAudit` | Get SQL audit log status |
| `getTDE` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tde` | Get TDE status |
| `listCluster` | `GET` | `/admin/v1/organizations/{orgName}/clusters` | List clusters in the Org |
| `listClusters` | `GET` | `/admin/v1/clusters` | Get cluster list |
| `listEndpoints` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/endpoints` | List cluster endpoints |
| `listInstance` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances` | List cluster instances |
| `listInstanceEvents` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/events` | List instance events |
| `listOfflineInstance` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/offlineInstances` | List offline cluster instances |
| `queryClusterMetrics` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/metrics` | Query cluster metrics |

## clusterAlertSwitch

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getClusterAlertDisabled` | `GET` | `/admin/v1/organizations/{orgName}/alerts/cluster/{clusterName}` | Check if cluster alert is disabled |

## clusterLog

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `aggregateSlowLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/aggregate` | Aggregate cluster slow logs |
| `getSlowLogStats` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/stats` | Get cluster slow log statistics |
| `getSlowLogTemplate` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates/{templateId}` | Get cluster slow log template |
| `queryAuditLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/audit` | Query cluster audit logs |
| `queryErrorLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/error` | Query cluster error logs |
| `queryLogHits` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/hits` | Query log hits histogram |
| `queryPodLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/pod` | Query cluster pod logs |
| `queryRunningLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/running` | Query cluster running logs |
| `querySlowLogs` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow` | Query cluster slow logs |
| `querySlowLogTemplates` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates` | Query cluster slow log templates |
| `querySlowLogTemplateSamples` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates/{templateId}/samples` | Query cluster slow log template samples |

## clusterTag

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getTags` | `GET` | `/admin/v1/organizations/{orgName}/clusterTags` | Get cluster tags |
| `listOrgTags` | `GET` | `/admin/v1/organizations/{orgName}/tags` | List tags by organization name |

## dameng

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getTablespace` | `GET` | `/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}` | Get Dameng tablespace info |
| `listTablespaces` | `GET` | `/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces` | List damengdb tablespaces |

## database

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getDatabase` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}` |  |
| `listDatabases` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases` | List cluster databases |

## databaseParameters

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listDatabaseParameters` | `GET` | `/admin/v1/databaseParameters` | List database parameters |

## diagnostics

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getDiagnosticsPostgresqlSession` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}` | Get PostgreSQL session basic diagnostics |
| `getDiagnosticsPostgresqlSessionLockAnalysis` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}/lockAnalysis` | Get PostgreSQL session lock analysis |
| `listDiagnosticsPostgresqlSessions` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions` | List PostgreSQL session basic diagnostics |

## disasterRecovery

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listDisasterRecovery` | `GET` | `/admin/v1/organizations/{orgName}/parent/{parentClusterID}/disasterRecovery` | List Disaster Recovery instances under the main cluster |

## dms

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getDataSourceV2` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}` | get the datasource |
| `getEngineAvailableConsole` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console` | get engine available console |
| `getMongoCollection` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}` | get MongoDB collection stats |
| `GetObjectInfo` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}/{objectName}` | get the detail object info |
| `getSchemaList` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/schemas` | list all databases or schema of the cluster |
| `GetTaskList` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/tasks` | Get the task list |
| `GetTaskProgress` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/task` | Get the task progress |
| `listDataSourceV2` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource` | list the datasource of a cluster |
| `listDmsDatabases` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/databases` | list all databases of the datasource |
| `listMongoCollections` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections` | list collections in a MongoDB database |
| `listMongoDatabaseMetadata` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/metadata` | list MongoDB database metadata |
| `listMongoDatabases` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases` | list MongoDB databases |
| `ListObjectNamesByType` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}` | list the all name for the specified object type |
| `ListObjectTypesInSchema` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}` | list the type and number of database objects in the specified database or schema |
| `listParameters` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameters` | list cluster parameters |
| `listQueryHistory` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/history` | list the query History |
| `listSessionsOld` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/sessions` | list all session for the cluster |
| `mongoAnalyzeSchema` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/schema` | analyze MongoDB collection schema from sample documents |
| `mongoGetShellPrompt` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/shell/sessions/{sessionID}/prompt` | get MongoDB mongosh session prompt |
| `mongoGetValidation` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/validation` | get MongoDB collection validation options |
| `mongoListIndexes` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/indexes` | list MongoDB collection indexes |
| `tenantParameterHistory` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameterHistory` | List parameters history of the Oceanbase tenant |

## engine

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `availableServiceVersion` | `GET` | `/admin/v1/environments/{environmentName}/engines/{engineName}/availableServiceVersion` | list the service version of the engine |
| `getEngineByNameInEnv` | `GET` | `/admin/v1/environments/{environmentName}/engines/{engineName}` | Get engine in environment |
| `getEngineLicenseEntity` | `GET` | `/admin/v1/engineLicenseEntity` | Get an engine license entity by ID |
| `getEngineNetworkModeOptions` | `GET` | `/admin/v1/environments/{environmentName}/engineNetworkModes/options` | Get available network modes for all engines from engineOption config |
| `getEngineNetworkModeSupported` | `GET` | `/admin/v1/environments/{environmentName}/engineNetworkModes/supported` | Get supported network modes for engine+mode from engineOption config |
| `GetUploadImageProgress` | `GET` | `/admin/v1/environments/{environmentName}/engines/{engineName}/imageUploadProgress` | get the progress of uploading image task |
| `listAllEngines` | `GET` | `/admin/v1/engines` | List all engines |
| `listEngineLicenseEntities` | `GET` | `/admin/v1/engineLicenseEntities` | List all engine license entities by license ID |
| `listEngineResourceConstraints` | `GET` | `/admin/v1/engines/resourceConstraints` | List engine resource constraints |
| `listEngineSchedulingPolicies` | `GET` | `/admin/v1/engines/{engineName}/schedulingPolicies` | List engine scheduling policies |
| `listEngineSchedulingRules` | `GET` | `/admin/v1/engines/{engineName}/schedulingRules` | List engine scheduling rules |
| `listEnginesInEnv` | `GET` | `/admin/v1/environments/{environmentName}/engines` | List engines in environment |
| `listEngineTypes` | `GET` | `/admin/v1/engineTypes` | List engine types |
| `listEngineVersions` | `GET` | `/admin/v1/engineVersions/{engineName}` | Get engine version list |
| `listEnvironmentEngineOptions` | `GET` | `/admin/v1/environments/{environmentName}/engineOptions` | List environment engine options |
| `ListServiceVersion` | `GET` | `/admin/v1/environments/{environmentName}/engines/{engineName}/serviceVersion` | list the service version of the engine |
| `ListUpgradeableServiceVersion` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/upgradeableServiceVersion` | list upgraded service version of the component |

## engineLicense

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `engineLicense` | `GET` | `/admin/v1/engineLicense` | Get engineLicense |
| `listEngineLicenses` | `GET` | `/admin/v1/engineLicenses` | List all engineLicenses |

## engineOption

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getEngineOption` | `GET` | `/admin/v1/engineOptions/{engineName}` | Get engineOption |
| `listEngineOptionHistory` | `GET` | `/admin/v1/engineOptionHistories` | List engineOption history |
| `listEngineOptions` | `GET` | `/admin/v1/engineOptions` | List all engineOptions |

## environment

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getEnvironment` | `GET` | `/admin/v1/environments/{environmentName}` | Get environment |
| `getEnvironmentBootstrapManifests` | `GET` | `/admin/v1/environments/{environmentName}/bootstrapManifests` | Get bootstrap manifests of an environment |
| `getEnvironmentCredential` | `GET` | `/admin/v1/environments/{environmentName}/credentials/{credentialName}` | Get environment credential |
| `getEnvironmentKubeconfig` | `GET` | `/admin/v1/environments/{environmentName}/kubeconfig` | Get environment kubeconfig |
| `getEnvironmentMetricsMonitorStats` | `GET` | `/admin/v1/environments/{environmentName}/nodes/monitorStatus` | Get environment MetricsMonitorStats |
| `getEnvironmentModuleDetails` | `GET` | `/admin/v1/environments/{environmentName}/modules/{moduleName}/details` | Get details information for an environment module |
| `getEnvironmentModuleInfo` | `GET` | `/admin/v1/environments/{environmentName}/modules` | Get environment module information in an environment |
| `getEnvironmentModuleLogs` | `GET` | `/admin/v1/environments/{environmentName}/modules/{moduleName}/pods/{podName}/logs` | Get logs for an environment module pod. When no parameters other than containerName and search are provided, start streaming logs in real-time. |
| `getEnvironmentProvisioningProgress` | `GET` | `/admin/v1/environments/{environmentName}/progress` | Get environment provisioning progress |
| `getEnvironmentStatus` | `GET` | `/admin/v1/environments/{environmentName}/status` | Get environment status |
| `getEnvironmentStatusHistory` | `GET` | `/admin/v1/environments/{environmentName}/statusHistory` | Get environment status history |
| `getLatestEnvModuleVersion` | `GET` | `/admin/v1/latestEnvModuleVersion` | Get environment module latest version |
| `getNode` | `GET` | `/admin/v1/environments/{environmentName}/nodes/{nodeName}` | Get node info |
| `getOptionalEnvironmentModules` | `GET` | `/admin/v1/environments/optional-modules` | get option environment module info |
| `listEnvironment` | `GET` | `/admin/v1/environments` | List environments |
| `listEnvironmentCredential` | `GET` | `/admin/v1/environments/{environmentName}/credentials` | List environment credentials |
| `listEnvNodeZone` | `GET` | `/admin/v1/environments/{environmentName}/availableZones` | List the availability zones where the environment's nodes are located |
| `listNodeGroups` | `GET` | `/admin/v1/environments/{environmentName}/nodeGroups` | List environment node groups |
| `listNodePod` | `GET` | `/admin/v1/environments/{environmentName}/nodes/{nodeName}/pods` | List Pod in the environment node |
| `listNodes` | `GET` | `/admin/v1/environments/{environmentName}/nodes` | List Kubernetes nodes in an environment |

## event

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getEvent` | `GET` | `/admin/v1/events/{eventID}` | Query event detail by Event ID |
| `getEventFilter` | `GET` | `/admin/v1/eventfilter/{filterType}` | Query available filters for event listing |
| `listEvents` | `GET` | `/admin/v1/events` | List events |
| `listOrgEvents` | `GET` | `/admin/v1/organizations/{orgName}/events` | List events |

## feature

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listFeature` | `GET` | `/admin/v1/features` | Get feature list |
| `listFeatureGroup` | `GET` | `/admin/v1/featureGroups` | Get feature group list |
| `readFeature` | `GET` | `/admin/v1/features/{featureName}` | Get feature |

## imageRegistry

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getImageRegistry` | `GET` | `/admin/v1/imageRegistries/{imageRegistryName}` | Get image registry |
| `listImageRegistries` | `GET` | `/admin/v1/imageRegistries` | List image registries |

## import

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getImportPreflightTask` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight/{taskId}` | Get preflight task details |
| `getImportTask` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}` | Get import task details |
| `listImportTask` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import` | Query import task list |

## inspection

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAggregateTaskResult` | `GET` | `/admin/v1/inspectionTasks/aggregate` | get aggregate task result |
| `getAutoInspection` | `GET` | `/admin/v1/autoInspection` | get auto inspection |
| `getInspectionTaskByEnv` | `GET` | `/admin/v1/environments/{environmentName}/inspectionTasksByEnv/{taskId}` | get inspection task by env |
| `getInspectionTaskByOrg` | `GET` | `/admin/v1/organizations/{orgName}/inspectionTasksByOrg/{taskId}` | get inspection task by org |
| `listAutoInspections` | `GET` | `/admin/v1/autoInspections` | list auto inspections |
| `listInspectionScripts` | `GET` | `/admin/v1/inspectionScripts` | list inspection scripts |
| `listInspectionTasksByEnv` | `GET` | `/admin/v1/environments/{environmentName}/inspectionTasksByEnv` | list inspection tasks by env |
| `listInspectionTasksByOrg` | `GET` | `/admin/v1/organizations/{orgName}/inspectionTasksByOrg` | list inspection tasks by org |

## instance

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listInstances` | `GET` | `/admin/v1/instances` | List cluster instances |

## ipWhitelist

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listIPWhitelist` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist` | List IP whitelists |

## kafka

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getKafkaBrokerConfigs` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers/{brokerId}/configs` | Get all configs of a broker |
| `getKafkaBrokers` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers` | Get all brokers in cluster |
| `getKafkaConsumerGroupDescribe` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups/{groupId}` | Get consumer group describe |
| `getKafkaTopicBrokers` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/brokers` | Get broker distributions of topic |
| `getKafkaTopicConfig` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/configs` | Get topic configuration |
| `getKafkaTopicInfos` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}` | Get topic Infos |
| `getKafkaTopicPartitions` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/partitions` | Get partition list of topic |
| `getKafkaTopics` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics` | Get all topics in cluster |
| `listKafkaConsumerGroups` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups` | List all consumer groups |
| `listKafkaTopicConsumerGroups` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups` | List consumer groups of topic |
| `listKafkaTopicConsumerOffsets` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets` | List consumer offsets of topic |
| `listKafkaTopicMessages` | `GET` | `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages` | List messages from topic |

## key

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getKey` | `GET` | `/admin/v1/keys/{keyName}` | get an existing key |
| `listKeys` | `GET` | `/admin/v1/keys` | List Keys |

## license

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getLicense` | `GET` | `/admin/v1/license` | Get license |

## llm

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getLLMByID` | `GET` | `/admin/v1/llm/{id}` | Get LLM by ID |
| `listAvailableModel` | `GET` | `/admin/v1/llm/models` | List available model |
| `listLLM` | `GET` | `/admin/v1/llm` | List LLM |

## loadBalancer

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getLoadBalancer` | `GET` | `/admin/v1/environments/{environmentName}/loadbalancer` | Get the load balancer info in the environment |

## member

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listOrgMember` | `GET` | `/admin/v1/organizations/{orgName}/members` | List members |
| `readOrgMember` | `GET` | `/admin/v1/organizations/{orgName}/members/{memberId}` | Get member |

## metering

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listMeteringTracks` | `GET` | `/admin/v1/metering/tracks` | List metering tracks |

## metrics

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAggregateMetaData` | `GET` | `/admin/v1/metrics/metaData/aggregate` | Get aggregate meta data |

## monitorDataSink

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listMonitorDataSinks` | `GET` | `/admin/v1/monitorDataSinks/environments/{environmentName}` | Get monitor data sink list |

## oceanbase

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getTenant` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}` | get tenants detail information of the oceanbase cluster |
| `listTenants` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenants` | list all tenants for the oceanbase cluster |

## opsrequest

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listAvailableNodes` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/rebuildInstance/availableNodes` | List available nodes for rebuilding instance |

## organization

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listOrganizations` | `GET` | `/admin/v1/organizations` | Get organization list |
| `readOrg` | `GET` | `/admin/v1/organizations/{orgName}` | Get organization |

## organizationParameter

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getOrgParameter` | `GET` | `/admin/v1/organizations/{orgName}/parameters/{parameterName}` | Get a parameter of an organization |
| `listOrgParameters` | `GET` | `/admin/v1/organizations/{orgName}/parameters` | List parameters of an organization |

## organizationResourceQuota

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `resourceQuotaAndUsage` | `GET` | `/admin/v1/organizations/{orgName}/resourceQuota` | Get the resource quota and usage of an organization |

## parameter

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listParameterProps` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameters` | List parameter properties of the cluster |
| `listParametersHistory` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterHistories` | List parameters history of the cluster |

## parameterTemplate

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getClusterParameterTemplate` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate` | Get cluster parameter template |
| `listParameterTemplates` | `GET` | `/admin/v1/parameterTemplates` | List parameter templates |
| `readParameterTemplate` | `GET` | `/admin/v1/parameterTemplate/{parameterTemplateName}` | Get parameter template details |
| `readParameterTemplateDiff` | `GET` | `/admin/v1/parameterTemplate/{parameterTemplateName}/diff` | Get parameter template diff against default template |

## platformComponent

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getPlatformComponent` | `GET` | `/admin/v1/platformComponents/{componentName}` | Get platform component detail |
| `listPlatformComponents` | `GET` | `/admin/v1/platformComponents` | List platform components |

## platformParameter

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getPlatformParameter` | `GET` | `/admin/v1/platformParameters/{platformParameterName}` | get platformParameter by name |
| `listPlatformParameters` | `GET` | `/admin/v1/platformParameters` | list platformParameters |

## postgresql

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listPGExtensions` | `GET` | `/admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions` | List PostgreSQL extensions |

## pricing

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getEnvironmentPricing` | `GET` | `/admin/v1/pricing` | Get the environment pricing |
| `getGlobalPricing` | `GET` | `/admin/v1/pricing/global` | Get the global information of pricing |

## project

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listProjects` | `GET` | `/admin/v1/environments/{environmentName}/projects` | List projects in an environment |

## provider

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getCloudProvider` | `GET` | `/admin/v1/providers/{providerName}` | Get cloud provider |
| `listCloudProviders` | `GET` | `/admin/v1/providers` | List cloud providers |

## RabbitMQ

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listRabbitAccounts` | `GET` | `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts` | List RabbitMQ accounts |
| `listRabbitExchanges` | `GET` | `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/exchanges` | List RabbitMQ exchanges |
| `listRabbitVHosts` | `GET` | `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/vhosts` | List RabbitMQ vhosts |

## rdbms

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getDatabaseOptions` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/dboptions` | get database options |

## recycleBinCluster

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getRecycleBinCluster` | `GET` | `/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}` | Get cluster in the Recycle Bin of the Org |
| `listRecycleBinCluster` | `GET` | `/admin/v1/organizations/{orgName}/recycleBin/clusters` | List clusters in the Recycle Bin of the Org |
| `listRecycleBinClusters` | `GET` | `/admin/v1/recycleBin/clusters` | List all clusters in the Recycle Bin |

## redis

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listRedisAccounts` | `GET` | `/admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts` | list redis accounts |

## relation

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listAvailableClustersForRelation` | `GET` | `/admin/v1/organizations/{orgName}/cluster/{clusterName}/available-relations` | list the available clusters for the organization to create the a relation |
| `listRelatedClusters` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/relations` | list the clusters that have built a relation to the specified cluster |

## resourceStats

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getResourceStats` | `GET` | `/admin/v1/environments/{environmentName}/resourceStats` | Get resource statistics of environment |
| `listInstancesResourceStats` | `GET` | `/admin/v1/environments/{environmentName}/nodes/{nodeName}/instances/resourceStats` | Get resource statistics of instances |
| `listNodesResourceStats` | `GET` | `/admin/v1/environments/{environmentName}/nodes/resourceStats` | Get resource statistics of nodes |

## restore

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `GetRestoreLog` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/restore/{restoreId}/logs` | get restore workload logs of the cluster |
| `getRestoreTimeRange` | `GET` | `/admin/v1/organizations/{orgName}/clustersWithDelete/restoreTimeRange` | Get cluster restore time ragne |
| `listClusterRestore` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/restore` | List restore tasks |
| `listRestores` | `GET` | `/admin/v1/restoreTasks` | List restore tasks |

## role

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getRoleByName` | `GET` | `/admin/v1/organizations/{orgName}/roles/{roleName}` | Get role by name |
| `listPermissions` | `GET` | `/admin/v1/permissions` | List all permissions |
| `listRolePermissions` | `GET` | `/admin/v1/organizations/{orgName}/roles/{roleName}/permissions` | List permissions of a role |
| `listRoles` | `GET` | `/admin/v1/organizations/{orgName}/roles` | List roles of a organization |

## session

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listSessions` | `GET` | `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions` | List cluster sessions |

## SLA

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `CalculateDailySLA` | `GET` | `/admin/v1/sla/daily` | Calculate daily SLA for a environment or a cluster since a specific date |
| `CalculateSLA` | `GET` | `/admin/v1/sla` | Calculate SLA for a environment |
| `GetSLASettingsInEnv` | `GET` | `/admin/v1/sla/settings` | Get SLA settings |
| `GetSLASupportEngines` | `GET` | `/admin/v1/sla/engines` | Get SLA supported engines |
| `ListEnvironmentOutageRecord` | `GET` | `/admin/v1/sla/outages` | List outage record for environments |
| `ListSLARank` | `GET` | `/admin/v1/sla/rank` | List SLA rank for a environment |
| `ListUncompliantClusters` | `GET` | `/admin/v1/sla/uncompliant` | List uncompliant clusters |

## storage

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getStorage` | `GET` | `/admin/v1/environments/{environmentName}/storages/{storageName}` | Get a storage |
| `listStorageProviders` | `GET` | `/admin/v1/storageProviders` | List storage providers for storage |
| `listStorages` | `GET` | `/admin/v1/environments/{environmentName}/storages` | List storages |

## storageClass

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getStorageClass` | `GET` | `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}` | get storage class |
| `listStorageClasses` | `GET` | `/admin/v1/environments/{environmentName}/storageClasses` | List storage classes of a environment |
| `listStorageClassNodeStats` | `GET` | `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/nodeStats` | get node stats of the storage class |
| `listStorageClassPvcs` | `GET` | `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/pvcs` | get persistentvolumeclaim list of the storage class |
| `listStorageProvisioners` | `GET` | `/admin/v1/environments/{environmentName}/storageProvisioners` | List the provisioners that can be used by storage class of a environment |

## task

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getTask` | `GET` | `/admin/v1/tasks/{taskId}` | Get task detail |
| `getTaskLog` | `GET` | `/admin/v1/tasks/{taskId}/log` | Get task log |
| `getTaskStepLog` | `GET` | `/admin/v1/tasks/{taskId}/steps/{stepId}/log` | Get task step log |
| `listTasks` | `GET` | `/admin/v1/tasks` | List task |
| `listTaskTypes` | `GET` | `/admin/v1/taskTypes` | List task types |

## tls

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getTLSCertificate` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tls` | Get cluster TLS certificate |

## user

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `getAuthenticatedUser` | `GET` | `/admin/v1/user` | Get authenticated user |
| `getUserAuthorization` | `GET` | `/admin/v1/users/{userID}/authorization` | Get user roles in multiple organizations |
| `listUsers` | `GET` | `/admin/v1/users` | List users |
| `readUserApikeys` | `GET` | `/admin/v1/user/apikeys` | Get apikeys of the authenticated user |

## vipPool

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listVIPPool` | `GET` | `/admin/v1/environments/{environmentName}/loadbalancer/vipPool` | List environment VIP Pools |

## vuln

| Operation ID | Method | Path | Summary |
|--------------|--------|------|---------|
| `listClusterVulns` | `GET` | `/admin/v1/organizations/{orgName}/clusters/{clusterName}/vulns` | List vulnerabilities which affected the cluster |
| `listVulns` | `GET` | `/admin/v1/vulns` | List vulnerabilities |
