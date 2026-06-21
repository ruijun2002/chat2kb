# List PostgreSQL session basic diagnostics

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/diagnostics/postgresql/sessions`
- **Operation ID:** `listDiagnosticsPostgresqlSessions`
- **Tags:** diagnostics

## Description

List PostgreSQL session basic diagnostics records. The response includes waitEventType and waitEvent so clients can identify lock-waiting sessions without loading lock rows.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `limit` | query | false | `integer` | Maximum number of sessions to return. Defaults to the backend limit when omitted. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/postgresqlSessionList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
