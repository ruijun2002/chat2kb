# List the availability zones where the environment's nodes are located

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/availableZones`
- **Operation ID:** `listEnvNodeZone`
- **Tags:** environment

## Description

List available zones of an environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the Environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/stringList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
