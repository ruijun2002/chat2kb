# get database options

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/dboptions`
- **Operation ID:** `getDatabaseOptions`
- **Tags:** rdbms, shared

## Description

get available options for creating database

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `type` | query | true | `string` | option type |
| `charset` | query | false | `string` | specified charset |
| `filter` | query | false | `string` | filter keyword |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get database options success | `application/json`: **Type:** `array` **Items:** **Type:** `string`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
