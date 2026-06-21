# Get import task details

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}`
- **Operation ID:** `getImportTask`
- **Tags:** import, shared

## Description

Gets detailed information about a specific import task by its ID

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `id` | path | true | `string` | Import task ID |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully returns import task details | `application/json`: **Ref:** `#/components/schemas/ImportTaskResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
