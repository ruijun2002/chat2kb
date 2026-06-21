# Calculate SLA for a environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla`
- **Operation ID:** `CalculateSLA`
- **Tags:** SLA

## Description

Calculate SLA for a environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `array` | name of the environment |
| `clusterID` | query | false | `array` | id of the cluster |
| `engine` | query | false | `array` | database engine type |
| `orgName` | query | false | `array` | name of the organization |
| `startTime` | query | true | `integer` | SLA calculation start time Unix timestamp, unit is second. |
| `endTime` | query | true | `integer` | SLA calculation end time Unix timestamp, unit is second. |
| `clusterNamePrefix` | query | false | `string` | Filter clusters by name prefix (fuzzy search). |
| `page` | query | false | `integer` | Page number for pagination, starts from 1. |
| `pageSize` | query | false | `integer` | Number of items per page. |
| `orderBy` | query | false | `string` | Order by field, available values are "clusterName", "engine". |
| `desc` | query | false | `boolean` | Whether to sort in descending order. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | SLA calculated successfully | `application/json`: **Ref:** `#/components/schemas/ClustersSLA`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
