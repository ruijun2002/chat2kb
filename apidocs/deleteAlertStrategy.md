# Delete alert strategy

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/alerts/strategies/{strategyId}`
- **Operation ID:** `deleteAlertStrategy`
- **Tags:** alertStrategy

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `strategyId` | path | true | `string` | id of the alert strategy |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
