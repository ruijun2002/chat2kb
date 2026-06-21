# Update SQL audit log status

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/sqlAudit`
- **Operation ID:** `updateSqlAudit`
- **Tags:** cluster, shared

## Description

Enable or disable SQL audit log for a cluster component

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/sqlAuditRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/sqlAuditResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
