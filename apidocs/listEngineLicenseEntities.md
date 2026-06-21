# List all engine license entities by license ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineLicenseEntities`
- **Operation ID:** `listEngineLicenseEntities`
- **Tags:** engine

## Description

list all engine license entities by license ID

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `licenseId` | query | true | `string` | license ID |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineLicenseEntityList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
