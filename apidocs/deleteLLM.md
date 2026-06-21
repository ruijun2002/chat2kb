# Delete LLM

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/llm/{id}`
- **Operation ID:** `deleteLLM`
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
| `204` | Returned when object is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
