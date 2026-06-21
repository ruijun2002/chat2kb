# Set alert object status

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alerts/objects/{alertId}`
- **Operation ID:** `setAlertObjectStatus`
- **Tags:** alertObject

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `alertId` | path | true | `string` | alert id |
| `status` | query | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertObject`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
