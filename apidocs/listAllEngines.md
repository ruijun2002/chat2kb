# List all engines

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engines`
- **Operation ID:** `listAllEngines`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
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
