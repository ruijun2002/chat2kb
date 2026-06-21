# List engine scheduling policies

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engines/{engineName}/schedulingPolicies`
- **Operation ID:** `listEngineSchedulingPolicies`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |
| `engineMode` | query | false | `string` | filter by engine mode |
| `env` | query | false | `string` | environment name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/engineSchedulingPolicy`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
