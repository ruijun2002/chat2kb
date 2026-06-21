# Delete role by name

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}`
- **Operation ID:** `deleteRoleByName`
- **Tags:** role, shared

## Description

Delete role by name

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
| `204` | Returned when role is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
