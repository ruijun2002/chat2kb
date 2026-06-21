# Cancel a task

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/tasks/{taskId}/cancel`
- **Operation ID:** `cancelTask`
- **Tags:** task

## Description

Cancel a task by taskID.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `taskId` | path | true | `string` | ID of the task |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Task cancelled successfully |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
