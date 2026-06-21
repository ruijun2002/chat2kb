# list inspection tasks by org

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/inspectionTasksByOrg`
- **Operation ID:** `listInspectionTasksByOrg`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterId` | query | false | `string` | list tasks for the specified cluster |
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
