# Get alert inhibit

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alerts/inhibits/{inhibitId}`
- **Operation ID:** `getAlertInhibit`
- **Tags:** alertInhibit

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `inhibitId` | path | true | `string` | inhibit id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertInhibit`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
