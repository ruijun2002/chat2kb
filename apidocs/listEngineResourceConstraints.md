# List engine resource constraints

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/engines/resourceConstraints`
- **Operation ID:** `listEngineResourceConstraints`
- **Tags:** engine, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engine` | query | false | `string` | engine name |
| `mode` | query | false | `string` | engine mode |
| `component` | query | false | `string` | engine component |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/resourceConstraintList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
