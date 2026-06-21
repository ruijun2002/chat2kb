# Patch alert inhibit

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alerts/inhibits`
- **Operation ID:** `patchAlertInhibit`
- **Tags:** alertInhibit

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertInhibit`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertInhibit`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
