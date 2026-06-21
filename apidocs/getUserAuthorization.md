# Get user roles in multiple organizations

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/users/{userID}/authorization`
- **Operation ID:** `getUserAuthorization`
- **Tags:** user

## Description

Get user roles in multiple organizations

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `userID` | path | true | `string` | ID of the user |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/userAuthorization`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
