# Update alert SMTP config

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alertSMTPConfig`
- **Operation ID:** `updateAlertSMTPConfig`
- **Tags:** alertSMTPConfig

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertSMTPConfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertSMTPConfig`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
