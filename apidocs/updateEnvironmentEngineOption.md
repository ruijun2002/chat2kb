# Update environment engine option

## Overview

- **Method:** `PUT`
- **Path:** `/admin/v1/environments/{environmentName}/engineOption/{id}`
- **Operation ID:** `updateEnvironmentEngineOption`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `id` | path | true | `string` | engine environment engine option record id |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentEngineOptionUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentEngineOption`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
