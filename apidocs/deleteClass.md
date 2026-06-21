# Delete class

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/classes`
- **Operation ID:** `deleteClass`
- **Tags:** class

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `code` | query | true | `string` | code |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
