# List all permissions for administrators

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/administrators/permissions`
- **Operation ID:** `listAdministratorsPermissions`
- **Tags:** administrator

## Description

List all permissions available for administrator roles

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminPermissionList`   |
| `401` |  |  |
