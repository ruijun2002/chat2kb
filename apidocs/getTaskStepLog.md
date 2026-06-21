# Get task step log

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/tasks/{taskId}/steps/{stepId}/log`
- **Operation ID:** `getTaskStepLog`
- **Tags:** task

## Description

Get logs for a specific task step (supports job type steps)

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `taskId` | path | true | `string` | ID of the task |
| `stepId` | path | true | `string` | ID of the step |
| `follow` | query | false | `boolean` | Follow log stream (streaming mode for running steps) |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
