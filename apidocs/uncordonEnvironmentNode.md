# Cordon environment node

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/uncordon`
- **Operation ID:** `uncordonEnvironmentNode`
- **Tags:** environment

## Description

cordon the specified Environment node

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
