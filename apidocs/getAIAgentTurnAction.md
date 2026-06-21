# Get one stable AI diagnosis turn process action

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}`
- **Operation ID:** `getAIAgentTurnAction`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `actionId` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | AI diagnosis process action detail | `application/json`: **Ref:** `#/components/schemas/aiAgentTurnAction`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
