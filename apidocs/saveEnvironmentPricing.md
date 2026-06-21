# Save the environment pricing

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/pricing`
- **Operation ID:** `saveEnvironmentPricing`
- **Tags:** pricing

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentPricing`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when information of pricing save successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
