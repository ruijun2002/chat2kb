# List available nodes for rebuilding instance

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/rebuildInstance/availableNodes`
- **Operation ID:** `listAvailableNodes`
- **Tags:** opsrequest, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `name` | query | true | `string` | name of the instance to be rebuilt |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Accepted | `application/json`: **Ref:** `#/components/schemas/nodeList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
