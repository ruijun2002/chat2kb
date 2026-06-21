# Get monitor data sink list

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/monitorDataSinks/environments/{environmentName}`
- **Operation ID:** `listMonitorDataSinks`
- **Tags:** monitorDataSink

## Description

Get monitor data sink list

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | kubernetes environment name which monitor data sink deployed in. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/monitorDataSinkList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
