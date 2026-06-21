# Get the task progress

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/task`
- **Operation ID:** `GetTaskProgress`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |
| `taskId` | query | true | `string` | the task id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Get the task success | `application/json`: **Ref:** `#/components/schemas/DmsTaskInfo`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
