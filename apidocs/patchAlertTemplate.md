# Update alert template

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/alertTemplates/{templateId}`
- **Operation ID:** `patchAlertTemplate`
- **Tags:** alertTemplate

## Description

partially update the alert receiver

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `templateId` | path | true | `string` | id of the alert tmpl configuration |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertTemplate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when project is deleted successfully. | `application/json`: **Ref:** `#/components/schemas/alertTemplate`   |
| `401` |  |  |
