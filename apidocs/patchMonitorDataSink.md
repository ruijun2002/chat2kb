# Update the specified monitor data sink

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/monitorDataSinks/{monitorDataSinkID}`
- **Operation ID:** `patchMonitorDataSink`
- **Tags:** monitorDataSink

## Description

Update the specified monitor data sink

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `monitorDataSinkID` | path | true | `string` | monitor data sink id |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/monitorDataSinkUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/monitorDataSink`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
