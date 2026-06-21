# Query cluster running logs

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/logs/running`
- **Operation ID:** `queryRunningLogs`
- **Tags:** clusterLog, shared

## Description

Query running logs of a cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `componentName` | query | false | `string` |  |
| `instanceName` | query | false | `string` |  |
| `filename` | query | false | `string` |  |
| `startTime` | query | true | `string` | Start time in epoch nanoseconds. |
| `endTime` | query | true | `string` | End time in epoch nanoseconds. |
| `limit` | query | false | `string` |  |
| `query` | query | false | `string` |  |
| `sortType` | query | false | `#/components/schemas/sortType` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/clusterRawLogResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
