# Get AI diagnosis agent status

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/status`
- **Operation ID:** `getAIAgentStatus`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis agent runtime status | `application/json`: **Ref:** `#/components/schemas/aiAgentRuntimeStatus`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
