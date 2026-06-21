# Get parameter template details

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/parameterTemplate/{parameterTemplateName}`
- **Operation ID:** `readParameterTemplate`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | true | `string` | name of the Org |
| `parameterTemplateName` | path | true | `string` | name of the parameter template |
| `partition` | query | false | `#/components/schemas/parameterTemplatePartition` | the template partition in read paramTpl request |
| `rawContent` | query | false | `boolean` | whether to return the raw template content |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | read parameter template successfully | `application/json`: **Ref:** `#/components/schemas/parameterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
