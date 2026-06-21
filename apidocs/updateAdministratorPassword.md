# Update administrator password

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/administrators/{administratorID}/password`
- **Operation ID:** `updateAdministratorPassword`
- **Tags:** administrator

## Description

Update administrator password

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` | ID of the administrator |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/password`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Password updated successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
