# Update engineOption

## Overview

- **Method:** `PUT`
- **Path:** `/admin/v1/engineOptions/{engineName}`
- **Operation ID:** `updateEngineOption`
- **Tags:** engineOption

## Description

Update a engineOption

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | Name of the engine |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineOption`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineOption`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
