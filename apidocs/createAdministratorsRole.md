# Create an administrator role

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/administrators/roles`
- **Operation ID:** `createAdministratorsRole`
- **Tags:** administrator

## Description

Create a custom administrator role

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/adminRoleCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Created | `application/json`: **Ref:** `#/components/schemas/adminRole`   |
| `400` |  |  |
| `401` |  |  |
