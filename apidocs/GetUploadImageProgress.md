# get the progress of uploading image task

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/engines/{engineName}/imageUploadProgress`
- **Operation ID:** `GetUploadImageProgress`
- **Tags:** engine, progress, serviceVersion

## Description

get the progress of uploading image task

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `engineName` | path | true | `string` | Name of the engine |
| `uploadId` | query | true | `string` | upload id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `object` **Properties:** uploadId, imageName, status, step, percentage   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
