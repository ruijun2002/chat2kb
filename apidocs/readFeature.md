# Get feature

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/features/{featureName}`
- **Operation ID:** `readFeature`
- **Tags:** feature, shared

## Description

Get feature

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `featureName` | path | true | `string` | name of the feature |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/feature`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
