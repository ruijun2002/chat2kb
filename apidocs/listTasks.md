# List task

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/tasks`
- **Operation ID:** `listTasks`
- **Tags:** task

## Description

List tasks

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | Filter by organization name |
| `resourceId` | query | false | `string` | Filter by resource ID (such as cluster ID, environment ID, etc.) |
| `resourceType` | query | false | `string` | Filter by resource type |
| `taskType` | query | false | `string` | Filter by task type (supports multiple task types separated by commas, e.g., "cluster-scale,cluster-upgrade") |
| `status` | query | false | `string` | Filter by task status (supports multiple statuses separated by commas, e.g., "Running,Pending") |
| `` |  | false | `` |  |
| `` |  | false | `` |  |
| `pageNumber` | query | false | `integer` | The pageNumber of the query |
| `pageSize` | query | false | `integer` | The pageSize of the query |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Current task list | `application/json`: **Ref:** `#/components/schemas/taskList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
