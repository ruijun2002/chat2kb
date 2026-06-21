# Delete alert receiver

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/alerts/receivers/{receiverId}`
- **Operation ID:** `deleteAlertReceiver`
- **Tags:** alertReceiver

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `receiverId` | path | true | `string` | receiver id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when alert receiver is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
