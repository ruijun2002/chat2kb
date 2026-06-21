# Get LLM by ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/llm/{id}`
- **Operation ID:** `getLLMByID`
- **Tags:** llm

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` | ID of the LLM |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | LLM by ID | `application/json`: **Ref:** `#/components/schemas/llm`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
