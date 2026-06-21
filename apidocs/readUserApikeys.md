# Get apikeys of the authenticated user

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/user/apikeys`
- **Operation ID:** `readUserApikeys`
- **Tags:** user, shared

## Description

Get apikeys of the authenticated user

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/apikeyList`   |
| `401` |  |  |
