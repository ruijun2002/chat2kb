# List all engineLicenses

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineLicenses`
- **Operation ID:** `listEngineLicenses`
- **Tags:** engineLicense, shared

## Description

list all engineLicenses

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | query | false | `string` | engine name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineLicenseList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
