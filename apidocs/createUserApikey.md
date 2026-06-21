# Create apikey of the authenticated user

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/user/apikeys`
- **Operation ID:** `createUserApikey`
- **Tags:** user, shared

## Description

Create apikey of the authenticated user

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/apikeyCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | A successful response. | `application/json`: **Ref:** `#/components/schemas/apikeyWithSK`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
