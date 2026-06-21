# Update an administrator role by name

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/administrators/roles/{roleName}`
- **Operation ID:** `updateAdministratorsRoleByName`
- **Tags:** administrator

## Description

Update a custom administrator role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `roleName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/adminRoleUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminRole`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
