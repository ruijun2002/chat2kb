# List engine scheduling rules

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engines/{engineName}/schedulingRules`
- **Operation ID:** `listEngineSchedulingRules`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |
| `engineMode` | query | false | `string` | filter by engine mode |
| `schedulingPolicyType` | query | false | `string` | filter by scheduling policy type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/engineSchedulingRule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
