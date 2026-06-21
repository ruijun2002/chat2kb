# Patch node group

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/nodeGroups/{nodeGroupName}`
- **Operation ID:** `patchNodeGroup`
- **Tags:** environment

## Description

partially update the specified NodeGroup

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the NodeGroup |
| `nodeGroupName` | path | true | `string` | name of the node group |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/nodeGroupUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/nodeGroup`   |
| `401` |  |  |
| `403` |  |  |
