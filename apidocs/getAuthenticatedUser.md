# Get authenticated user

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/user`
- **Operation ID:** `getAuthenticatedUser`
- **Tags:** user

## Description

Get authenticated login user info

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/user`   |
| `401` |  |  |
