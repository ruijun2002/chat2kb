# Delete an AI diagnosis conversation

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}`
- **Operation ID:** `deleteAIAgentConversation`
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
| `200` | AI diagnosis conversation deleted | `application/json`: **Ref:** `#/components/schemas/aiAgentDeleteConversationResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `500` |  |  |
