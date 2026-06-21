# Query import task list

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import`
- **Operation ID:** `listImportTask`
- **Tags:** import, shared

## Description

Gets import task list for specified cluster, supports filtering by status and pagination

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully returns task list with pagination info | `application/json`: **Ref:** `#/components/schemas/ImportTaskListResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
