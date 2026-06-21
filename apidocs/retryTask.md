# Retry a task

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/tasks/{taskId}/retry`
- **Operation ID:** `retryTask`
- **Tags:** task

## Description

retry task

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `taskId` | path | true | `string` | ID of the task |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Current status of the task | `application/json`: **Ref:** `#/components/schemas/task`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
