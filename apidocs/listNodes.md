# List Kubernetes nodes in an environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/nodes`
- **Operation ID:** `listNodes`
- **Tags:** environment

## Description

List Kubernetes nodes in an environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `hostName` | query | false | `string` | Hostname to filter by |
| `outOfTopologyRange` | query | false | `boolean` | List nodes with invalid region & zone labels |
| `labelKey` | query | false | `string` | List nodes with label |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A list of nodes | `application/json`: **Ref:** `#/components/schemas/nodeList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
