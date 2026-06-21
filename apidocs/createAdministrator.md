# Create a new administrator

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/administrators`
- **Operation ID:** `createAdministrator`
- **Tags:** administrator

## Description

Create a new administrator

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/userCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Created | `application/json`: **Ref:** `#/components/schemas/user`   |
| `400` |  |  |
| `401` |  |  |
| `409` |  |  |
