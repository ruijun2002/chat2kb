# List environment engine options

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engineOptions`
- **Operation ID:** `listEnvironmentEngineOptions`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `engineName` | query | false | `string` | filter by engine name |
| `mode` | query | false | `string` | filter by engine mode |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentEngineOptionList`   |
| `401` |  |  |
| `403` |  |  |
