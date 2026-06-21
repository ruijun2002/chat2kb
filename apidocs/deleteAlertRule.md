# Delete alert rule

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/alerts/rules/{alertName}`
- **Operation ID:** `deleteAlertRule`
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
| `204` | Delete successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
