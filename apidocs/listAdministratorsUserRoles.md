# List roles of an administrator user

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/administrators/{administratorID}/roles`
- **Operation ID:** `listAdministratorsUserRoles`
- **Tags:** administrator

## Description

List all roles assigned to a specific administrator user

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/adminRoleList`   |
| `401` |  |  |
| `404` |  |  |
