# Check if storage can be accessed

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/storageCheck`
- **Operation ID:** `checkStorage`
- **Tags:** storage

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/storageCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/storageCheckResult`   |
| `401` |  |  |
| `403` |  |  |
