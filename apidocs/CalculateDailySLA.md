# Calculate daily SLA for a environment or a cluster since a specific date

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla/daily`
- **Operation ID:** `CalculateDailySLA`
- **Tags:** SLA

## Description

Calculate daily SLA for a environment or a cluster since a specific date

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `array` | name of the environment |
| `startTime` | query | true | `integer` | SLA calculation start time Unix timestamp, unit is second. |
| `endTime` | query | true | `integer` | SLA calculation end time Unix timestamp, unit is second. |
| `clusterID` | query | false | `array` | id of the cluster |
| `engine` | query | false | `array` | database engine type |
| `orgName` | query | false | `array` | name of the organization |
| `timezoneOffset` | query | false | `integer` | timezone offset in seconds, e.g. offset of UTC+08:00 is +8 * 60 * 60, default is 0 |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | SLA calculated successfully | `application/json`: **Ref:** `#/components/schemas/DailySLAList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
