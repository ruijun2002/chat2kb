# Create import task

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import`
- **Operation ID:** `createImportTask`
- **Tags:** import, shared

## Description

Creates new data import task based on data source configuration and import options

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ImportTaskCreateRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Task created successfully, returns basic task information | `application/json`: **Ref:** `#/components/schemas/ImportTaskResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
