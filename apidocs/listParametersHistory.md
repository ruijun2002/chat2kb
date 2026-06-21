# List parameters history of the cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterHistories`
- **Operation ID:** `listParametersHistory`
- **Tags:** parameter, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `parameterName` | query | false | `string` | name of the parameter |
| `component` | query | true | `string` | component type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get parameters history of the cluster successfully | `application/json`: **Ref:** `#/components/schemas/parameterHistoryList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
