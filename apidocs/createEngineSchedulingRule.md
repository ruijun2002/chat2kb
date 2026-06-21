# Create engine scheduling rule

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engines/{engineName}/schedulingRules`
- **Operation ID:** `createEngineSchedulingRule`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | engine name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineSchedulingRule`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineSchedulingRule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
