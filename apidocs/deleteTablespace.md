# Delete damengdb tablespace

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces/{tablespaceName}`
- **Operation ID:** `deleteTablespace`
- **Tags:** dameng

## Description

Delete tablespace for a Dameng cluster.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |
| `tablespaceName` | path | true | `string` | Tablespace name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | A successful response. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
