# Approve one AI diagnosis tool confirmation

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/tool-confirmations/{confirmationId}/approve`
- **Operation ID:** `approveAIAgentToolConfirmation`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `confirmationId` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/aiAgentToolConfirmationDecisionRequest`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Tool confirmation approved | `application/json`: **Ref:** `#/components/schemas/aiAgentToolConfirmationDecisionResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `500` |  |  |
