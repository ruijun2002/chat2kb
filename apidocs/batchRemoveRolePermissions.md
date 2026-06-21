# Batch remove permissions from a role

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}/permissions/batch`
- **Operation ID:** `batchRemoveRolePermissions`
- **Tags:** role, shared

## Description

Batch remove permissions from a role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `roleName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Type:** `array` **Items:** **Type:** `string`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when permissions are removed successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
