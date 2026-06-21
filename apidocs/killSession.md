# Kill cluster session

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions/{session}`
- **Operation ID:** `killSession`
- **Tags:** session, rdbms, shared

## Description

kill a session in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `session` | path | true | `string` | session id |
| `keep` | query | false | `boolean` | if keep is true, the session will not be killed but only closed |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when session is killed successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
