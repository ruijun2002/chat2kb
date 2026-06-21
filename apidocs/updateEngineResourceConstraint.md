# Update engine resource constraint

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/engines/resourceConstraints/{id}`
- **Operation ID:** `updateEngineResourceConstraint`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` | id of the engine resource constraint |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/resourceConstraintUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Operation completed successfully | `application/json`: **Ref:** `#/components/schemas/resourceConstraint`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
