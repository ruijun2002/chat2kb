# list auto inspections

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/autoInspections`
- **Operation ID:** `listAutoInspections`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `resourceType` | query | true | `#/components/schemas/autoInspectionResourceType` | type of the auto inspection |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/autoInspection`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
