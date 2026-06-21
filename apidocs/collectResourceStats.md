# Collect resource statistics of environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/resourceStats/collect`
- **Operation ID:** `collectResourceStats`
- **Tags:** resourceStats

## Description

Triggers an immediate collection of resource statistics for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | The name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
