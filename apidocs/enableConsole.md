# enable console

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console`
- **Operation ID:** `enableConsole`
- **Tags:** dms, shared

## Description

enable console

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/DMSConsoleEnableOpt`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | enable console successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
