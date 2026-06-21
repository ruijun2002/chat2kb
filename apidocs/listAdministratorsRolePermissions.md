# List permissions of an administrator role

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/administrators/roles/{roleName}/permissions`
- **Operation ID:** `listAdministratorsRolePermissions`
- **Tags:** administrator

## Description

List all permissions assigned to a specific administrator role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `roleName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminPermissionList`   |
| `401` |  |  |
| `404` |  |  |
