# Get node info

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodes/{nodeName}`
- **Operation ID:** `getNode`
- **Tags:** environment

## Description

Get specified node info for environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `nodeName` | path | true | `string` | name of the environment node |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/jsonBody`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
