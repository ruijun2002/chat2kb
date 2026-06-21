# Get engine in environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engines/{engineName}`
- **Operation ID:** `getEngineByNameInEnv`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the EnvironmentName |
| `engineName` | path | true | `string` | name of the engine |
| `version` | query | true | `string` | engine version |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engine`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
