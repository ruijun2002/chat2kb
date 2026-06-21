# Query log hits histogram

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/hits`
- **Operation ID:** `queryLogHits`
- **Tags:** clusterLog, shared

## Description

Query log hits histogram for time-bucketed log counts (VictoriaLogs only). When logType=slow, buckets also include avgExecutionTime in seconds; templateId can be supplied for slow template trends.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `startTime` | query | true | `string` | Start time in epoch nanoseconds. |
| `endTime` | query | true | `string` | End time in epoch nanoseconds. |
| `step` | query | true | `string` | Time bucket size, e.g. 5s, 30s, 1m, 5m, 30m, 1h |
| `logType` | query | true | `string` | Log type: runninglog, errorlog, slow, auditlog |
| `componentName` | query | false | `string` |  |
| `instanceName` | query | false | `string` |  |
| `query` | query | false | `string` |  |
| `minExecutionTime` | query | false | `number` | Minimum slow log execution time in seconds. Only applies when logType=slow. |
| `maxExecutionTime` | query | false | `number` | Maximum slow log execution time in seconds. Only applies when logType=slow. |
| `minLockTime` | query | false | `number` | Minimum slow log lock time in seconds. Only applies when logType=slow. |
| `maxLockTime` | query | false | `number` | Maximum slow log lock time in seconds. Only applies when logType=slow. |
| `minRowsExamined` | query | false | `integer` |  |
| `maxRowsExamined` | query | false | `integer` |  |
| `minRowsSent` | query | false | `integer` |  |
| `maxRowsSent` | query | false | `integer` |  |
| `dbName` | query | false | `string` | Filter slow logs whose database name contains this value. |
| `userName` | query | false | `string` | Filter slow logs whose user name contains this value. |
| `clientIp` | query | false | `string` | Filter slow logs whose client IP contains this value, or is within this CIDR range when the value is valid CIDR. |
| `appName` | query | false | `string` | Filter slow logs whose application name contains this value. |
| `templateId` | query | false | `string` |  |
| `unclassifiedOnly` | query | false | `boolean` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/clusterLogHitsResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
