# get aggregate task result

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/inspectionTasks/aggregate`
- **Operation ID:** `getAggregateTaskResult`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `aggregateType` | query | true | `#/components/schemas/aggregateTaskType` | the type of the aggregate task |
| `engine` | query | false | `string` | the engine of the task |
| `resourceName` | query | false | `string` | only show the result of the specific organization or environment |
| `resultType` | query | false | `#/components/schemas/aggregateTaskResultType` | result of the task |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/aggregateTaskResultList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
