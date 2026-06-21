# Query available filters for event listing

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/eventfilter/{filterType}`
- **Operation ID:** `getEventFilter`
- **Tags:** event

## Description

Query available filters for event listing

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `filterType` | path | true | `#/components/schemas/eventFilterType` | The event filter field you want to obtain. |
| `source` | query | true | `string` | The event filter you want to query from a certain source. |
| `resourceType` | query | false | `string` | The resource type you want to obtain. |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/eventFilterOptionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
