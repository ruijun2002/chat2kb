# Get cluster slow log template

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/slow/templates/{templateId}`
- **Operation ID:** `getSlowLogTemplate`
- **Tags:** clusterLog, shared

## Description

Get a slow log template of a cluster (VictoriaLogs backend only)

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `templateId` | path | true | `string` |  |
| `startTime` | query | true | `string` | Start time in epoch nanoseconds. |
| `endTime` | query | true | `string` | End time in epoch nanoseconds. |
| `componentName` | query | false | `string` |  |
| `instanceName` | query | false | `string` |  |
| `query` | query | false | `string` |  |
| `minExecutionTime` | query | false | `number` | Minimum slow log execution time in seconds. Decimal values are supported, for example 0.5. |
| `maxExecutionTime` | query | false | `number` | Maximum slow log execution time in seconds. Decimal values are supported, for example 0.5. |
| `minLockTime` | query | false | `number` | Minimum slow log lock time in seconds. Decimal values are supported, for example 0.001. |
| `maxLockTime` | query | false | `number` | Maximum slow log lock time in seconds. Decimal values are supported, for example 0.001. |
| `minRowsExamined` | query | false | `integer` |  |
| `maxRowsExamined` | query | false | `integer` |  |
| `minRowsSent` | query | false | `integer` |  |
| `maxRowsSent` | query | false | `integer` |  |
| `dbName` | query | false | `string` | Filter slow logs whose database name contains this value. |
| `userName` | query | false | `string` | Filter slow logs whose user name contains this value. |
| `clientIp` | query | false | `string` | Filter slow logs whose client IP contains this value, or is within this CIDR range when the value is valid CIDR. |
| `appName` | query | false | `string` | Filter slow logs whose application name contains this value. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/clusterSlowLogTemplate`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
