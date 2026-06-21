# Update license

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/license`
- **Operation ID:** `updateLicense`
- **Tags:** license

## Description

Update license

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/licenseRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/license`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
