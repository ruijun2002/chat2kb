# List all engineOptions

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineOptions`
- **Operation ID:** `listEngineOptions`
- **Tags:** engineOption, shared

## Description

list all engineOptions

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `version` | query | false | `#/components/schemas/engineOptionVersion` | The version of the engineOption to query, `current` from potentially modified data, `original` from the json files of the apiserver |
| `filterLoadBackupFromOfflineInstance` | query | false | `boolean` | Whether to filter load backup from offline instance |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/engineOptionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
