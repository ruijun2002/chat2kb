# Create alert receiver

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alerts/receivers`
- **Operation ID:** `createAlertReceiver`
- **Tags:** alertReceiver

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `category` | query | true | `#/components/schemas/alertReceiverCategory` | alert receiver category |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertReceiver`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertReceiver`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
