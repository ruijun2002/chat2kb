# Batch remove permissions from an administrator role

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/administrators/roles/{roleName}/permissions/batch`
- **Operation ID:** `batchRemoveAdministratorsRolePermissions`
- **Tags:** administrator

## Description

Remove multiple permissions from a custom administrator role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `roleName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Type:** `array` **Items:** **Type:** `string`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when permissions are removed successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
