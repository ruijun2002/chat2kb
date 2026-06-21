# Get role by name

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/roles/{roleName}`
- **Operation ID:** `getRoleByName`
- **Tags:** role, shared

## Description

Get role by name

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
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/role`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
