# Get SQL audit log status

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/sqlAudit`
- **Operation ID:** `getSqlAudit`
- **Tags:** cluster, shared

## Description

Query the SQL audit log switch status for a cluster component

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `component` | query | true | `string` | component type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/sqlAuditStatus`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
