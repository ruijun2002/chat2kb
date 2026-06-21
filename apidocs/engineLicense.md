# Get engineLicense

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineLicense`
- **Operation ID:** `engineLicense`
- **Tags:** engineLicense

## Description

Get a engineLicense detail

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `licenseId` | query | true | `string` | license id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineLicense`   |
| `401` |  |  |
| `403` |  |  |
