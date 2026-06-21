# Get resource statistics of instances

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/instances/resourceStats`
- **Operation ID:** `listInstancesResourceStats`
- **Tags:** resourceStats

## Description

Returns aggregated resource statistics for the specified node.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | The name of the environment |
| `nodeName` | path | true | `string` | The name of the node |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/instanceResourceStatsList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
