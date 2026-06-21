# Remove a role from an administrator user

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/administrators/{administratorID}/roles/{roleName}`
- **Operation ID:** `removeAdministratorsUserRole`
- **Tags:** administrator

## Description

Remove a specific role from an administrator user

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` |  |
| `roleName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when role is removed successfully. |  |
| `401` |  |  |
| `404` |  |  |
