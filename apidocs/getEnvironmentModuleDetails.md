# Get details information for an environment module

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/modules/{moduleName}/details`
- **Operation ID:** `getEnvironmentModuleDetails`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Environment Name |
| `moduleName` | path | true | `string` | Environment module name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/environmentModuleDetails`   |
| `400` |  |  |
| `404` |  |  |
| `500` |  |  |
