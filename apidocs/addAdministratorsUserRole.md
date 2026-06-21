# Add a role to an administrator user

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/administrators/{administratorID}/roles`
- **Operation ID:** `addAdministratorsUserRole`
- **Tags:** administrator

## Description

Assign a role to a specific administrator user

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Type:** `object` **Properties:** roleName

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when role is assigned successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `404` |  |  |
