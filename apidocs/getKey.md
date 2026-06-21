# get an existing key

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/keys/{keyName}`
- **Operation ID:** `getKey`
- **Tags:** key

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `keyName` | path | true | `string` | the name of key |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully updated the key | `application/json`: **Ref:** `#/components/schemas/key`   |
| `401` |  |  |
| `403` |  |  |
