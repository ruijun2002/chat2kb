# Get platform component detail

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/platformComponents/{componentName}`
- **Operation ID:** `getPlatformComponent`
- **Tags:** platformComponent

## Description

Get platform component detail by name, including monitoring and log query metadata

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `componentName` | path | true | `string` | Platform component name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/platformComponentDetails`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
