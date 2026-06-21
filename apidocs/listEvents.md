# List events

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/events`
- **Operation ID:** `listEvents`
- **Tags:** event

## Description

List events

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `status` | query | false | `#/components/schemas/eventResultStatus` | the status of the event |
| `customQuery` | query | false | `string` | Advanced query conditions, supporting all types of filterType. Such as "orgID:111 orgID:222 operatorID:333" |
| `pageNumber` | query | false | `integer` | the pageNumber of the query |
| `pageSize` | query | false | `integer` | the pageSize of the query |
| `` |  | false | `` |  |
| `` |  | false | `` |  |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/eventList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
