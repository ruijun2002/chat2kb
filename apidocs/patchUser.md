# Update the information of the specified user

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/users/{userID}`
- **Operation ID:** `patchUser`
- **Tags:** user

## Description

Update the information of the specified user

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `userID` | path | true | `string` | ID of the user |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/userUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/user`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
