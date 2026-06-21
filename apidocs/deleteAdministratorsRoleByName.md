# Delete an administrator role by name

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/administrators/roles/{roleName}`
- **Operation ID:** `deleteAdministratorsRoleByName`
- **Tags:** administrator

## Description

Delete a custom administrator role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `roleName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when role is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
