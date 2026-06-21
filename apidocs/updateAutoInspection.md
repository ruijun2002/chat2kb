# update auto inspection

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/autoInspections/{id}`
- **Operation ID:** `updateAutoInspection`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | path | true | `string` | id of the auto inspection |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/autoInspection`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/autoInspection`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
