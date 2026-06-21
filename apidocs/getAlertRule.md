# Get alert rule

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alerts/rules/{alertName}`
- **Operation ID:** `getAlertRule`
- **Tags:** alertRule

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `alertName` | path | true | `string` | name of the alert rule |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertRule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
