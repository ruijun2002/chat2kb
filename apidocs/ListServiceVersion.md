# list the service version of the engine

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engines/{engineName}/serviceVersion`
- **Operation ID:** `ListServiceVersion`
- **Tags:** engine, shared

## Description

list the service version of the engine

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `engineName` | path | true | `string` | Name of the engine |
| `engineMode` | query | true | `string` | engine mode |
| `engineVersion` | query | true | `string` | engine version |
| `component` | query | false | `string` | component type, refer to componentDef and support NamePrefix |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineServiceVersions`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
