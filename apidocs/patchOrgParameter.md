# Update a parameter of an organization

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/parameters/{parameterName}`
- **Operation ID:** `patchOrgParameter`
- **Tags:** organizationParameter, shared

## Description

Update a parameter of an organization

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |
| `parameterName` | path | true | `string` | The name of the parameter |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgParameter`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgParameter`   |
