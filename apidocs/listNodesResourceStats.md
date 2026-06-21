# Get resource statistics of nodes

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/resourceStats`
- **Operation ID:** `listNodesResourceStats`
- **Tags:** resourceStats, shared

## Description

Returns aggregated resource statistics for the specified environment within an organization.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | The name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/nodeResourceStatsList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
