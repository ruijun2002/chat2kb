# Create environment engine option

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/engineOptions`
- **Operation ID:** `createEnvironmentEngineOption`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentEngineOptionCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentEngineOption`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
