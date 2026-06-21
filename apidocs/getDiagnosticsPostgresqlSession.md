# Get PostgreSQL session basic diagnostics

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}`
- **Operation ID:** `getDiagnosticsPostgresqlSession`
- **Tags:** diagnostics

## Description

Get one PostgreSQL session basic diagnostics record by backend pid.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `pid` | path | true | `integer` | PostgreSQL backend process id. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/postgresqlSession`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
