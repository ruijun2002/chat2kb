# Delete a storage

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/storages/{storageName}`
- **Operation ID:** `deleteStorage`
- **Tags:** storage

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `storageName` | path | true | `string` | name of the storage |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
