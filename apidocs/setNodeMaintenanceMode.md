# Set the node to maintenance mode

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/maintenance/on`
- **Operation ID:** `setNodeMaintenanceMode`
- **Tags:** environment

## Description

Set the node to maintenance mode. This action temporarily disables the node for maintenance activities, ensuring no new workloads are scheduled on it.

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
