# Delete environment node group

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/nodeGroups/{nodeGroupName}`
- **Operation ID:** `deleteNodeGroup`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `nodeGroupName` | path | true | `string` | name of the node group |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
