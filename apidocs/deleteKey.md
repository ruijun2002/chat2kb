# Delete a specific key

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/keys/{keyName}`
- **Operation ID:** `deleteKey`
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
| `204` | Successfully deleted the key |  |
| `401` |  |  |
| `403` |  |  |
