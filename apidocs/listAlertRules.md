# List alert rules

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alerts/rules`
- **Operation ID:** `listAlertRules`
- **Tags:** alertRule

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `disabled` | query | false | `boolean` | disabled status |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertRuleList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
