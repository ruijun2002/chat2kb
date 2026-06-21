# Get image registry

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/imageRegistries/{imageRegistryName}`
- **Operation ID:** `getImageRegistry`
- **Tags:** imageRegistry

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `imageRegistryName` | path | true | `string` | name of the image registry |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/imageRegistry`   |
| `403` |  |  |
| `404` |  |  |
