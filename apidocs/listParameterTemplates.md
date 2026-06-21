# List parameter templates

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/parameterTemplates`
- **Operation ID:** `listParameterTemplates`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | name of the Org |
| `partition` | query | false | `#/components/schemas/parameterTemplatePartition` | the template partition in listParameterTemplates request |
| `version` | query | false | `string` | Cluster Application Version |
| `component` | query | false | `string` | component type |
| `engineName` | query | false | `string` | engine Name |
| `engineMode` | query | false | `string` | engine mode |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list parameter templates successfully | `application/json`: **Ref:** `#/components/schemas/paramTplList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
