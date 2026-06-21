# get inspection task by org

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/inspectionTasksByOrg/{taskId}`
- **Operation ID:** `getInspectionTaskByOrg`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `taskId` | path | true | `string` | list task details if specified |
| `format` | query | false | `#/components/schemas/inspectionTaskFormat` | the format of the task |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/inspectionTask`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
