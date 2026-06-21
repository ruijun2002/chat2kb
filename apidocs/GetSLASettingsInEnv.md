# Get SLA settings

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla/settings`
- **Operation ID:** `GetSLASettingsInEnv`
- **Tags:** SLA

## Description

Get SLA settings in a environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | true | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | SLA settings retrieved successfully | `application/json`: **Ref:** `#/components/schemas/SLASettings`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
