# Delete apikey

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/user/apikey/{keyName}`
- **Operation ID:** `deleteApikey`
- **Tags:** user, shared

## Description

delete apikey

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `keyName` | path | true | `string` | Name of the Apikey |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when apikey is deleted successfully. |  |
| `401` |  |  |
| `404` |  |  |
