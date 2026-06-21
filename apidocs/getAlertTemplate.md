# Get alert template

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alertTemplates/{templateId}`
- **Operation ID:** `getAlertTemplate`
- **Tags:** alertTemplate

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `templateId` | path | true | `string` | id of the alert tmpl configuration |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertTemplate`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
