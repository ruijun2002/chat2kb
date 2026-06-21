# List engineOption history

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engineOptionHistories`
- **Operation ID:** `listEngineOptionHistory`
- **Tags:** engineOption

## Description

List a engineOption histories of a engine

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | query | true | `string` | Name of the engine |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineOptionHistoryList`   |
| `401` |  |  |
| `403` |  |  |
