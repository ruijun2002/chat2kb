# List storages

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storages`
- **Operation ID:** `listStorages`
- **Tags:** storage

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `name` | query | false | `string` | the search key to search storage's name |
| `key` | query | false | `string` | key to search storage's tag |
| `value` | query | false | `string` | value to search storage's tag |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/storageList`   |
| `401` |  |  |
| `403` |  |  |
