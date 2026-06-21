# Download a generated AI diagnosis report artifact

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/ai-agent/conversations/{conversationId}/turn-actions/{actionId}/artifacts/{artifactId}/download`
- **Operation ID:** `downloadAIAgentTurnActionArtifact`
- **Tags:** AI Agent

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `conversationId` | path | true | `string` |  |
| `actionId` | path | true | `string` |  |
| `artifactId` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Generated report artifact content | `application/octet-stream`: **Type:** `string`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
| `503` |  |  |
