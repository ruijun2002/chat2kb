# Get preflight task details

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight/{taskId}`
- **Operation ID:** `getImportPreflightTask`
- **Tags:** import, shared

## Description

Retrieves detailed information about a specific data import preflight task by its ID

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `taskId` | path | true | `string` | Preflight task ID |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully returns preflight task details | `application/json`: **Ref:** `#/components/schemas/preCheckTaskDetail`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
