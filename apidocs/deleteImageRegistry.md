# Delete image registry

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/imageRegistries/{imageRegistryName}`
- **Operation ID:** `deleteImageRegistry`
- **Tags:** imageRegistry

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `imageRegistryName` | path | true | `string` | name of the image registry |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/imageRegistry`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
