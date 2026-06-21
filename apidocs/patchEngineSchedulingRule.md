# Patch engine scheduling rule

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/engines/{engineName}/schedulingRules/{ruleId}`
- **Operation ID:** `patchEngineSchedulingRule`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |
| `ruleId` | path | true | `string` | id of the engine scheduling rule |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineSchedulingRule`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineSchedulingRule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
