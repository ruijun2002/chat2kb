# Get an AI diagnosis conversation

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}`
- **Operation ID:** `getAIAgentConversation`
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
| `200` | AI diagnosis conversation | `application/json`: **Ref:** `#/components/schemas/aiAgentConversation`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
