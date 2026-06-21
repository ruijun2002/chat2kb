# Get cluster slow log statistics

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/stats`
- **Operation ID:** `getSlowLogStats`
- **Tags:** clusterLog, shared

## Description

Get statistics summary for slow logs of a cluster. When the same slow log filters are supplied, totalSlowLogs can be used as the filtered list preview count.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `startTime` | query | true | `string` | Start time in epoch nanoseconds. |
| `endTime` | query | true | `string` | End time in epoch nanoseconds. |
| `componentName` | query | false | `string` |  |
| `instanceName` | query | false | `string` |  |
| `query` | query | false | `string` |  |
| `minExecutionTime` | query | false | `number` | Minimum execution time in seconds. Decimal values are supported, for example 0.5. |
| `maxExecutionTime` | query | false | `number` | Maximum execution time in seconds. Decimal values are supported, for example 0.5. |
| `minLockTime` | query | false | `number` | Minimum lock time in seconds. Decimal values are supported, for example 0.001. |
| `maxLockTime` | query | false | `number` | Maximum lock time in seconds. Decimal values are supported, for example 0.001. |
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
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/clusterSlowLogStats`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
