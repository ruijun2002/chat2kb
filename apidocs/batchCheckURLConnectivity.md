# Batch check URLs connectivity

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/alerts/checkURL`
- **Operation ID:** `batchCheckURLConnectivity`
- **Tags:** alert, shared

## Description

Tests multiple URLs for connectivity in parallel

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/URLCheck`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/URLCheck`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
