# Update alert receiver

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alerts/receivers/{receiverId}`
- **Operation ID:** `updateAlertReceiver`
- **Tags:** alertReceiver

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `receiverId` | path | true | `string` | receiver id |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertReceiver`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when project is deleted successfully. | `application/json`: **Ref:** `#/components/schemas/alertReceiver`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
