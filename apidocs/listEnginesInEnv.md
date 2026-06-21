# List engines in environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engines`
- **Operation ID:** `listEnginesInEnv`
- **Tags:** engine, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the EnvironmentName |
| `name` | query | false | `string` | engine name |
| `type` | query | false | `string` | engine Type |
| `version` | query | false | `string` | engine version |
| `provider` | query | false | `string` | engine provider |
| `all` | query | false | `boolean` | list all engines include uninstall engines |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
