# Get cluster parameter template

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate`
- **Operation ID:** `getClusterParameterTemplate`
- **Tags:** parameterTemplate, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `component` | query | false | `string` | component type |
| `engineName` | query | false | `string` | engine name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get parameter template applicable to the cluster successfully | `application/json`: **Ref:** `#/components/schemas/paramTplApplyToClusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
