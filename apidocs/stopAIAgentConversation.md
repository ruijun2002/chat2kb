# Stop the current AI diagnosis turn

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/stop`
- **Operation ID:** `stopAIAgentConversation`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis conversation stopped | `application/json`: **Ref:** `#/components/schemas/aiAgentStopConversationResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
