# List environment node groups

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodeGroups`
- **Operation ID:** `listNodeGroups`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `zones` | query | false | `array` | available zones for filtering node groups |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when environment is created successfully. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/nodeGroup`   |
| `403` |  |  |
| `404` |  |  |
