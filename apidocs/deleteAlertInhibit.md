# Delete alert inhibit

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/alerts/inhibits/{inhibitId}`
- **Operation ID:** `deleteAlertInhibit`
- **Tags:** alertInhibit

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `inhibitId` | path | true | `string` | inhibit id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
