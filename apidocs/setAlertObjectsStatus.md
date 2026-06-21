# Set alert objects status

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alerts/objects`
- **Operation ID:** `setAlertObjectsStatus`
- **Tags:** alertObject

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `status` | query | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Type:** `array` **Items:** **Ref:** `#/components/schemas/alertObject`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertObjectList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
