# Update user password

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/users/{userID}/password`
- **Operation ID:** `updateUserPassword`
- **Tags:** user

## Description

Update user password

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `userID` | path | true | `string` | ID of the user |

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
