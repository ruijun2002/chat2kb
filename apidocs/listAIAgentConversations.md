# List AI diagnosis conversations

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations`
- **Operation ID:** `listAIAgentConversations`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `limit` | query | false | `integer` |  |
| `after` | query | false | `string` |  |
| `clusterName` | query | false | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis conversations | `application/json`: **Ref:** `#/components/schemas/aiAgentConversationList`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
