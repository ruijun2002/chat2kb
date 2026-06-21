# add LLM

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/llm`
- **Operation ID:** `addLLM`
- **Tags:** llm

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | orgName the LLM belongs to |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/llm`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when object is created successfully. | `application/json`: **Ref:** `#/components/schemas/llm`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
