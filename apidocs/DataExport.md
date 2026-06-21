# Data Export

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/export`
- **Operation ID:** `DataExport`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/DmsExportRequest`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | data in format |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
