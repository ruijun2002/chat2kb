# List damengdb tablespaces

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces`
- **Operation ID:** `listTablespaces`
- **Tags:** dameng

## Description

List tablespaces for a Dameng cluster.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/DmTablespaceList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
