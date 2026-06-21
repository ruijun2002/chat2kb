# list inspection tasks by env

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/inspectionTasksByEnv`
- **Operation ID:** `listInspectionTasksByEnv`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `nodeName` | query | false | `string` | list tasks for the specified node |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/inspectionTask`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
