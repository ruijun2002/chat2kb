# Get task detail

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/tasks/{taskId}`
- **Operation ID:** `getTask`
- **Tags:** task

## Description

Get task

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
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
