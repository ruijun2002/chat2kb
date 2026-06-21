# List stable AI diagnosis turn process actions

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions`
- **Operation ID:** `listAIAgentTurnActions`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `turnId` | query | false | `string` |  |
| `after` | query | false | `string` |  |
| `limit` | query | false | `integer` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Stable AI diagnosis process actions | `application/json`: **Ref:** `#/components/schemas/aiAgentTurnActionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
