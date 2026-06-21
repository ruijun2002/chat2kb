# update platformParameters

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/platformParameters`
- **Operation ID:** `updatePlatformParameters`
- **Tags:** platformParameter

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Type:** `array` **Items:** **Ref:** `#/components/schemas/platformParameterUpdate`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/platformParameter`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
