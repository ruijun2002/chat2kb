# Get a class type by ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/classTypes/{id}`
- **Operation ID:** `getClassType`
- **Tags:** classTypes

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/classType`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
