# Get parameter template diff against default template

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/parameterTemplate/{parameterTemplateName}/diff`
- **Operation ID:** `readParameterTemplateDiff`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | true | `string` | name of the Org |
| `parameterTemplateName` | path | true | `string` | name of the parameter template |
| `partition` | query | false | `#/components/schemas/parameterTemplatePartition` | the template partition in diff parameter template request |
| `rawContent` | query | false | `boolean` | whether to compare raw template content |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get parameter template diff successfully | `application/json`: **Ref:** `#/components/schemas/parameterTemplateDiff`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
