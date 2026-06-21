# Batch add permissions to a role

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}/permissions/batch`
- **Operation ID:** `batchAddRolePermissions`
- **Tags:** role, shared

## Description

Batch add permissions to a role

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
| `204` | Returned when permissions are added successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
