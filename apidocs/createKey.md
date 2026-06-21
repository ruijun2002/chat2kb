# Create a new key

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/keys`
- **Operation ID:** `createKey`
- **Tags:** key

## Description

Store a new key in the system.

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/key`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | key created successfully. | `application/json`: **Ref:** `#/components/schemas/key`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
