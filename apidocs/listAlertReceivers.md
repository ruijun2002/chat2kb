# List alert receivers

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alerts/receivers`
- **Operation ID:** `listAlertReceivers`
- **Tags:** alertReceiver

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `category` | query | false | `#/components/schemas/alertReceiverCategory` | alert receiver category |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertReceiverList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
