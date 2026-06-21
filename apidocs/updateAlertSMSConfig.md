# Update alert SMS config

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alertSMSConfig`
- **Operation ID:** `updateAlertSMSConfig`
- **Tags:** alertConfig

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertSMSConfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertSMSConfig`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
