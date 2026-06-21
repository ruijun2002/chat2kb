# List database parameters

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/databaseParameters`
- **Operation ID:** `listDatabaseParameters`
- **Tags:** databaseParameters

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | query | true | `string` | engine Name |
| `component` | query | true | `string` | component type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list database parameters successfully | `application/json`: **Ref:** `#/components/schemas/databaseParameterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
