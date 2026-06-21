# Update the information of the specified administrator

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/administrators/{administratorID}`
- **Operation ID:** `patchAdministrator`
- **Tags:** administrator

## Description

Update the information of the specified administrator

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` | ID of the administrator |

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
