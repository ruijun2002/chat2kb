# Delete engine scheduling rule

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/engines/{engineName}/schedulingRules/{ruleId}`
- **Operation ID:** `deleteEngineSchedulingRule`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |
| `ruleId` | path | true | `string` | id of the engine scheduling rule |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when engine scheduling rule is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
