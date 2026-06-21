# Delete alert template

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/alertTemplates/{templateId}`
- **Operation ID:** `deleteAlertTemplate`
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
| `204` | Returned when project is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
