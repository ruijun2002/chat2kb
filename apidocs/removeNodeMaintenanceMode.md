# Remove the node from maintenance mode

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/maintenance/off`
- **Operation ID:** `removeNodeMaintenanceMode`
- **Tags:** environment

## Description

Remove the node from maintenance mode. This action restores the node to its normal operational state, allowing it to resume handling workloads.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `nodeName` | path | true | `string` | name of the environment node |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/jsonBody`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
