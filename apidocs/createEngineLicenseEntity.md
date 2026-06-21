# Create a new engine license entity

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engineLicenseEntity`
- **Operation ID:** `createEngineLicenseEntity`
- **Tags:** engine

## Description

create a new engine license entity

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineLicenseEntityCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineLicenseEntity`   |
| `401` |  |  |
| `403` |  |  |
