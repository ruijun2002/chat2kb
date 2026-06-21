# Patch engine scheduling policy

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/engines/{engineName}/schedulingPolicies`
- **Operation ID:** `patchEngineSchedulingPolicy`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |
| `engineMode` | query | true | `string` | filter by engine mode |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineSchedulingPolicy`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineSchedulingPolicy`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
