# Create a new user

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/users`
- **Operation ID:** `createUser`
- **Tags:** user

## Description

Create a new user

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
