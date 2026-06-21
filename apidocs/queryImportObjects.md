# Query replication objects for import

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/objects`
- **Operation ID:** `queryImportObjects`
- **Tags:** import, shared

## Description

Enumerates replication objects (databases, schemas, tables, etc.) for the requested node. The metadata levels depend on the source engine (for example MySQL uses `database -> table`, PostgreSQL uses `schema -> table`).

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ImportQueryObjectsRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Object tree nodes retrieved successfully | `application/json`: **Ref:** `#/components/schemas/replicationObjectTree`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `501` |  |  |
