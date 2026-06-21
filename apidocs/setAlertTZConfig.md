# Set alert timezone config

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alerts/config`
- **Operation ID:** `setAlertTZConfig`
- **Tags:** alertConfig

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertConfig`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertConfig`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
