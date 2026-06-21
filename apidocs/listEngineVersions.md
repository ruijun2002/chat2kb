# Get engine version list

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineVersions/{engineName}`
- **Operation ID:** `listEngineVersions`
- **Tags:** engine

## Description

Get engine version list

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | Name of Engine. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineVersionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
