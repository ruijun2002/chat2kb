# Get environment status

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/status`
- **Operation ID:** `getEnvironmentStatus`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentStatus`   |
| `403` |  |  |
| `404` |  |  |
