# List alert objects

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/alerts/objects`
- **Operation ID:** `listAlertObjects`
- **Tags:** alertObject

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `page` | query | false | `integer` | page number |
| `pageSize` | query | false | `integer` | page size |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertObjectList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
