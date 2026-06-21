# Get environment module information in an environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/modules`
- **Operation ID:** `getEnvironmentModuleInfo`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Environment Name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/environmentModuleInfo`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `429` |  |  |
| `500` |  |  |
