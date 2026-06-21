# Delete parameter template

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/parameterTemplate/{parameterTemplateName}`
- **Operation ID:** `deleteParameterTemplate`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | true | `string` | name of the Org |
| `parameterTemplateName` | path | true | `string` | name of the parameter template |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
