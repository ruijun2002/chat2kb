# Delete environment engine option

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/engineOption/{id}`
- **Operation ID:** `deleteEnvironmentEngineOption`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `id` | path | true | `string` | engine environment engine option id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | No Content |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
