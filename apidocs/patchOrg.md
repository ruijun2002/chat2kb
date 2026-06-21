# Update organization

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}`
- **Operation ID:** `patchOrg`
- **Tags:** organization, shared

## Description

partially update the specified Org

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/org`   |
| `201` | Created | `application/json`: **Ref:** `#/components/schemas/org`   |
| `401` |  |  |
| `403` |  |  |
