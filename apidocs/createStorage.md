# Create a storage

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/storages`
- **Operation ID:** `createStorage`
- **Tags:** storage

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/storageCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/storage`   |
| `401` |  |  |
| `403` |  |  |
