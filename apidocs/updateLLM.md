# Update LLM

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/llm/{id}`
- **Operation ID:** `updateLLM`
- **Tags:** llm

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` | ID of the LLM |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/llm`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when object is updated successfully. | `application/json`: **Ref:** `#/components/schemas/llm`   |
| `403` |  |  |
| `404` |  |  |
