# Create an AI diagnosis conversation

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations`
- **Operation ID:** `createAIAgentConversation`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/aiAgentCreateConversationRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis conversation | `application/json`: **Ref:** `#/components/schemas/aiAgentConversation`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
