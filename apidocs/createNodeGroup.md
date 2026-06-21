# Create environment node group

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/nodeGroups`
- **Operation ID:** `createNodeGroup`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/nodeGroup`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when environment is created successfully. | `application/json`: **Ref:** `#/components/schemas/nodeGroup`   |
| `403` |  |  |
| `404` |  |  |
