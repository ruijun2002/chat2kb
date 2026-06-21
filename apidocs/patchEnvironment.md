# Update environment

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}`
- **Operation ID:** `patchEnvironment`
- **Tags:** environment

## Description

partially update the specified Environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/environment`   |
| `401` |  |  |
| `403` |  |  |
