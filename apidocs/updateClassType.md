# Update a class type by ID

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/classTypes/{id}`
- **Operation ID:** `updateClassType`
- **Tags:** classTypes

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/createClassType`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/classType`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
