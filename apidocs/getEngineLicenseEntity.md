# Get an engine license entity by ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineLicenseEntity`
- **Operation ID:** `getEngineLicenseEntity`
- **Tags:** engine

## Description

get an engine license entity by ID

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `entityId` | query | true | `string` | entity ID |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineLicenseEntity`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
