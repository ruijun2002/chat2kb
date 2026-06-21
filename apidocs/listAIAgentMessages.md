# List AI diagnosis conversation messages

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/messages`
- **Operation ID:** `listAIAgentMessages`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `after` | query | false | `string` |  |
| `limit` | query | false | `integer` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis messages | `application/json`: **Ref:** `#/components/schemas/aiAgentMessageList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
