# Batch update parameters of an organization

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/parameters`
- **Operation ID:** `batchUpdateOrgParameters`
- **Tags:** organizationParameter, shared

## Description

Batch update parameters of an organization

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgParameterList`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgParameterList`   |
| `401` |  |  |
| `403` |  |  |
