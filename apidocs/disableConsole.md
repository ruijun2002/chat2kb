# disable console

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/console`
- **Operation ID:** `disableConsole`
- **Tags:** dms, shared

## Description

disable console

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | disable console successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
