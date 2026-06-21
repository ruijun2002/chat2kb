# List uncompliant clusters

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla/uncompliant`
- **Operation ID:** `ListUncompliantClusters`
- **Tags:** SLA

## Description

List uncompliant clusters that sla lower than the threshold

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `array` | name of the environment |
| `engine` | query | false | `array` | database engine type |
| `orgName` | query | false | `array` | name of the organization |
| `startTime` | query | true | `integer` | SLA calculation start time Unix timestamp, unit is second. |
| `endTime` | query | true | `integer` | SLA calculation end time Unix timestamp, unit is second. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Uncompliant clusters retrieved successfully | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/SLA`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
