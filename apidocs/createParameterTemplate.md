# Create parameter template

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/parameterTemplates`
- **Operation ID:** `createParameterTemplate`
- **Tags:** parameterTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/paramTplCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | create parameter template successfully | `application/json`: **Ref:** `#/components/schemas/paramTplListItem`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
