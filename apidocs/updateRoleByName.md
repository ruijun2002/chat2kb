# Update role by name

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}`
- **Operation ID:** `updateRoleByName`
- **Tags:** role, shared

## Description

Update role by name

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `roleName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/roleUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/role`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
