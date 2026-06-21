# List all administrator roles

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/administrators/roles`
- **Operation ID:** `listAdministratorsRoles`
- **Tags:** administrator

## Description

List all administrator roles including built-in and custom roles

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminRoleList`   |
| `401` |  |  |
