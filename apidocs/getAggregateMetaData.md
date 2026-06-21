# Get aggregate meta data

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/metrics/metaData/aggregate`
- **Operation ID:** `getAggregateMetaData`
- **Tags:** metrics

## Description

Get aggregate meta data including total count and time series

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `metaData` | query | true | `#/components/schemas/aggregateMetaDataType` |  |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/aggregateMetaData`   |
| `401` |  |  |
| `403` |  |  |
