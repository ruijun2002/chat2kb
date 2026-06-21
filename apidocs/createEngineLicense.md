# Create engineLicense

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engineLicense`
- **Operation ID:** `createEngineLicense`
- **Tags:** engineLicense

## Description

Create a new engineLicense

## Parameters

_No parameters._

## Request Body

**Content-Type:** `multipart/form-data`
**Ref:** `#/components/schemas/engineLicenseCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineLicense`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
