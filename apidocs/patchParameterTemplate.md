# Update parameter template

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/parameterTemplate/{parameterTemplateName}`
- **Operation ID:** `patchParameterTemplate`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | true | `string` | name of the Org |
| `parameterTemplateName` | path | true | `string` | name of the parameter template |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/paramTplUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/paramTplListItem`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
