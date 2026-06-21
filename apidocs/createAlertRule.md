# Create alert rule

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alerts/rules`
- **Operation ID:** `createAlertRule`
- **Tags:** alertRule

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `disabled` | query | false | `boolean` | disabled status |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertRule`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertRule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
