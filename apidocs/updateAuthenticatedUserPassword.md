# Update current authenticated user password

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/user/password`
- **Operation ID:** `updateAuthenticatedUserPassword`
- **Tags:** user

## Description

Update current authenticated user password.

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Type:** `object` **Properties:** new_password

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Password updated successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
