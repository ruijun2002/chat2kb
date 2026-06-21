# Undrain environment node

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/undrain`
- **Operation ID:** `undrainEnvironmentNode`
- **Tags:** environment

## Description

Undrain the specified Environment node. This action will remove the NoExecute taint and make the node schedulable again.

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
| `204` | No Content |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
