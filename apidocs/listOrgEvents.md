# List events

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/events`
- **Operation ID:** `listOrgEvents`
- **Tags:** event, shared

## Description

List events

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization Name |
| `customQuery` | query | false | `string` | Advanced query conditions, supporting all types of filterType. Such as "operatorID:333 operatorID:444" |
| `status` | query | false | `#/components/schemas/eventResultStatus` | the status of the event |
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
