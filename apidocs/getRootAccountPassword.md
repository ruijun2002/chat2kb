# get root account password

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/root-password`
- **Operation ID:** `getRootAccountPassword`
- **Tags:** account, shared

## Description

get root account password

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | query | true | `string` | name of the account |
| `component` | query | false | `string` | name of the component |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get root account password success | `application/json`: **Type:** `string`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
| `500` |  |  |
