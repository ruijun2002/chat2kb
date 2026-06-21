# Get available network modes for all engines from engineOption config

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engineNetworkModes/options`
- **Operation ID:** `getEngineNetworkModeOptions`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineNetworkModeOptions`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
