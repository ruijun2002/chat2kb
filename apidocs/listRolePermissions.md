# List permissions of a role

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}/permissions`
- **Operation ID:** `listRolePermissions`
- **Tags:** role, shared

## Description

List permissions of a role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `roleName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/permissionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
