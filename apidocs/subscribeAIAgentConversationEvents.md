# Subscribe to AI diagnosis conversation events

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/events`
- **Operation ID:** `subscribeAIAgentConversationEvents`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `after` | query | false | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis event stream | `text/event-stream`: **Ref:** `#/components/schemas/aiAgentEvent`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
