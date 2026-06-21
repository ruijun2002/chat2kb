# get inspection task by env

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/inspectionTasksByEnv/{taskId}`
- **Operation ID:** `getInspectionTaskByEnv`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `taskId` | path | true | `string` | list task details if specified |
| `format` | query | false | `#/components/schemas/inspectionTaskFormat` | the format of the task |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/inspectionTaskItem`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
