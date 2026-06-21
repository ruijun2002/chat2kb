# Create monitor data sink

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/monitorDataSinks`
- **Operation ID:** `createMonitorDataSink`
- **Tags:** monitorDataSink

## Description

Create monitor data sink

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/monitorDataSinkCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/monitorDataSink`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
