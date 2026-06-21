# Get an administrator role by name

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/administrators/roles/{roleName}`
- **Operation ID:** `getAdministratorsRoleByName`
- **Tags:** administrator

## Description

Get detailed information about a specific administrator role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `roleName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminRole`   |
| `401` |  |  |
| `404` |  |  |
