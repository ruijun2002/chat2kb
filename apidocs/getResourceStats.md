# Get resource statistics of environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/resourceStats`
- **Operation ID:** `getResourceStats`
- **Tags:** resourceStats

## Description

Returns aggregated resource statistics for the specified environment within an organization.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | The name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentResourceStats`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
