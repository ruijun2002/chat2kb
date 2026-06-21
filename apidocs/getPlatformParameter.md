# get platformParameter by name

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/platformParameters/{platformParameterName}`
- **Operation ID:** `getPlatformParameter`
- **Tags:** platformParameter, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `platformParameterName` | path | true | `string` | name of the platformParameter |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/platformParameter`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
