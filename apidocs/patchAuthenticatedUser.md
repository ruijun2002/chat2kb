# Update user information

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/user`
- **Operation ID:** `patchAuthenticatedUser`
- **Tags:** user

## Description

partially update the specified User. If you want to update phone number, you must request /api/v1/user/phone-verification-code first.

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/userUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/user`   |
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
