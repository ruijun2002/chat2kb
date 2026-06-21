# Manage engine in environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/engines/{engineName}`
- **Operation ID:** `engineAction`
- **Tags:** engine

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the EnvironmentName |
| `engineName` | path | true | `string` | name of the engine |

## Request Body

**Content-Type:** `application/json`
**Type:** `object` **Properties:** version, action, id

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Operation completed successfully | `application/json`: **Type:** `string` Success message indicating the operation result   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
