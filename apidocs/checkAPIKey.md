# check apikey available

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/llm/check`
- **Operation ID:** `checkAPIKey`
- **Tags:** llm, shared

## Description

check apikey available

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/llm`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | apikey available | `application/json`: **Ref:** `#/components/schemas/checkAPIKey`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
