# List classes

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/classes`
- **Operation ID:** `listClasses`
- **Tags:** class, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | query | false | `string` | filter by engine name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/class`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
