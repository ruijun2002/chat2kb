# Send a user message and start or continue AI diagnosis

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/messages`
- **Operation ID:** `sendAIAgentMessage`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/aiAgentSendMessageRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis message accepted | `application/json`: **Ref:** `#/components/schemas/aiAgentSendMessageResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `500` |  |  |
| `503` |  |  |
