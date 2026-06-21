# List SLA rank for a environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla/rank`
- **Operation ID:** `ListSLARank`
- **Tags:** SLA

## Description

List SLA rank for a environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `array` | name of the environment |
| `engine` | query | false | `array` | database engine type |
| `orgName` | query | false | `array` | name of the organization |
| `startTime` | query | true | `integer` | SLA calculation start time Unix timestamp, unit is second. |
| `endTime` | query | true | `integer` | SLA calculation end time Unix timestamp, unit is second. |
| `limit` | query | false | `integer` | Number of items per page. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | SLA calculated successfully | `application/json`: **Ref:** `#/components/schemas/SLAList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
