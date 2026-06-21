# Restore organization's alert rule configuration to defaults

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alerts/rules/reset`
- **Operation ID:** `restoreOrgAlertRuleToDefault`
- **Tags:** alertRule

## Description

Restores the alert rule configuration for a specific organization to the system default settings.

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Alert rule configuration for the organization restored to defaults successfully. | `application/json`: **Type:** `object` **Properties:** message   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
