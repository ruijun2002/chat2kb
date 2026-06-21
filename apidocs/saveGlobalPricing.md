# Save the global information of pricing

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/pricing/global`
- **Operation ID:** `saveGlobalPricing`
- **Tags:** pricing

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/globalPricing`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when global information of pricing save successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
