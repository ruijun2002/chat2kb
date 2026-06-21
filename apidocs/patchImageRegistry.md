# Update image registry

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/imageRegistries/{imageRegistryName}`
- **Operation ID:** `patchImageRegistry`
- **Tags:** imageRegistry

## Description

partially update the specified image registry

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `imageRegistryName` | path | true | `string` | name of the image registry |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/imageRegistry`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/imageRegistry`   |
| `401` |  |  |
| `403` |  |  |
