# delete user

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/users/{userID}`
- **Operation ID:** `deleteUser`
- **Tags:** user

## Description

delete user

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `userID` | path | true | `string` | ID of the user |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
