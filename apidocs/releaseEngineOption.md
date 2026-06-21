# Release engineOption

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engineOptions/{engineName}/release`
- **Operation ID:** `releaseEngineOption`
- **Tags:** engineOption

## Description

Release a engineOption

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | Name of the engineOption |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineOption`   |
| `401` |  |  |
| `403` |  |  |
