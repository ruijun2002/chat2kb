# enable the service version of the engine

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/engines/{engineName}/serviceVersion`
- **Operation ID:** `EnableServiceVersion`
- **Tags:** enableServiceVersion

## Description

enable the service version of the engine and create related resources

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `engineName` | path | true | `string` | Name of the engine |

## Request Body

**Content-Type:** `application/json`
**Type:** `object` **Properties:** serviceVersion, engineVersion
**Content-Type:** `multipart/form-data`
**Type:** `object` the data of image to upload **Properties:** image

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Type:** `object` the id of the upload task **Properties:** uploadId   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
