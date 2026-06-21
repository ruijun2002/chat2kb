# Delete import task

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/{id}`
- **Operation ID:** `deleteImportTask`
- **Tags:** import, shared

## Description

Stops and deletes specified import task, will clean up related Kubernetes resources

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
| `204` | Task deleted successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
