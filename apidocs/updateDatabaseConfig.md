# update database config

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases/{databaseName}`
- **Operation ID:** `updateDatabaseConfig`
- **Tags:** database, rdbms, shared

## Description

update a database config in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `databaseName` | path | true | `string` | name of database |

## Request Body

**Content-Type:** `application/json`
**Type:** `object`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
