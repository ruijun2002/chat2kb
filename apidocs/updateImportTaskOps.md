# Create a import task operation

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}/ops/{opsType}`
- **Operation ID:** `updateImportTaskOps`
- **Tags:** import, shared

## Description

Performs pause or resume operation on import task based on opsType parameter

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `id` | path | true | `string` | Import task ID |
| `opsType` | path | true | `#/components/schemas/ImportOpsType` | Operation type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Import task operation completed successfully | `application/json`: **Ref:** `#/components/schemas/ImportTaskResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
