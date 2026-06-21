# Batch add permissions to an administrator role

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/administrators/roles/{roleName}/permissions/batch`
- **Operation ID:** `batchAddAdministratorsRolePermissions`
- **Tags:** administrator

## Description

Add multiple permissions to a custom administrator role

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
| `204` | Returned when permissions are added successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
