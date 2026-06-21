# Get engineOption

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineOptions/{engineName}`
- **Operation ID:** `getEngineOption`
- **Tags:** engineOption, shared

## Description

Get a engineOption detail

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | Name of the engine |
| `version` | query | false | `#/components/schemas/engineOptionVersion` | The version of the engineOption to query, `current` from potentially modified data, `original` from the json files of the apiserver |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineOption`   |
| `401` |  |  |
| `403` |  |  |
