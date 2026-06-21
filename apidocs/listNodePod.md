# List Pod in the environment node

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}/pods`
- **Operation ID:** `listNodePod`
- **Tags:** environment

## Description

List Pod in the environment node

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `nodeName` | path | true | `string` | name of the environment node |
| `type` | query | true | `string` | filter Pods by type, supported types [all, kube-system, kb-system, cluster], default all if not provided |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/listBody`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
