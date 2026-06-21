# List parameter properties of the cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameters`
- **Operation ID:** `listParameterProps`
- **Tags:** parameter, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |
| `component` | query | false | `string` | component type |
| `rawContent` | query | false | `boolean` | whether to return the raw template content |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get configuration of the cluster successfully | `application/json`: **Ref:** `#/components/schemas/parameterList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
