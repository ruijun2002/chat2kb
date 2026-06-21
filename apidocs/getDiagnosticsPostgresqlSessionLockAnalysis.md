# Get PostgreSQL session lock analysis

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions/{pid}/lockAnalysis`
- **Operation ID:** `getDiagnosticsPostgresqlSessionLockAnalysis`
- **Tags:** diagnostics

## Description

Get read-only lock analysis for one PostgreSQL backend pid from the current DMS PostgreSQL lock snapshot.

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
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/postgresqlLockAnalysis`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
