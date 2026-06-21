# Get feature list

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/features`
- **Operation ID:** `listFeature`
- **Tags:** feature, shared

## Description

Get feature list

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `group` | query | false | `string` | name of the feature group |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/featureList`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
