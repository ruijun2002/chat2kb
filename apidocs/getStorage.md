# Get a storage

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storages/{storageName}`
- **Operation ID:** `getStorage`
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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/storage`   |
| `401` |  |  |
| `403` |  |  |
