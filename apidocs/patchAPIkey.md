# Update apikey information

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/user/apikey/{keyName}`
- **Operation ID:** `patchAPIkey`
- **Tags:** user, shared

## Description

partially update the specified apikey

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `keyName` | path | true | `string` | Name of the apikey |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/apikeyCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/apikey`   |
| `401` |  |  |
