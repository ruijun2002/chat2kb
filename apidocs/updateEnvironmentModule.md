# update environment module

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/modules`
- **Operation ID:** `updateEnvironmentModule`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Environment Name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentModuleUpdate`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Type:** `object` **Properties:** taskId   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `429` |  |  |
| `500` |  |  |
