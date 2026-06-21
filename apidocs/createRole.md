# Create role

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/roles`
- **Operation ID:** `createRole`
- **Tags:** role, shared

## Description

Create role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/roleCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/role`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
