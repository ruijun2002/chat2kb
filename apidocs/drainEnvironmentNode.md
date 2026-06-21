# Drain environment node

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/drain`
- **Operation ID:** `drainEnvironmentNode`
- **Tags:** environment

## Description

Drain the specified Environment node. This action will evict all pods from the node and mark it as unschedulable.

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
