# Update SLA settings

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/sla/settings`
- **Operation ID:** `UpdateSLASettingsInEnv`
- **Tags:** SLA

## Description

Update SLA settings in a environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/SLASettings`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | SLA settings updated successfully |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
