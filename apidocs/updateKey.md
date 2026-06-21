# Update an existing key

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/keys/{keyName}`
- **Operation ID:** `updateKey`
- **Tags:** key

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `keyName` | path | true | `string` | the name of key |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/key`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully updated the key | `application/json`: **Ref:** `#/components/schemas/key`   |
| `401` |  |  |
| `403` |  |  |
