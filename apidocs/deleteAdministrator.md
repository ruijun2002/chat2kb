# delete administrator

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/administrators/{administratorID}`
- **Operation ID:** `deleteAdministrator`
- **Tags:** administrator

## Description

delete administrator

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `administratorID` | path | true | `string` | ID of the administrator |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
