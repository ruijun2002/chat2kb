# create MongoDB collection

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}`
- **Operation ID:** `mongoCreateCollection`
- **Tags:** dms

## Description

Creates a collection. Creating the first collection in a database is the supported Create Database backend semantic.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |
| `db` | path | true | `string` | database name |
| `col` | path | true | `string` | initial collection name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/MongoCreateCollectionRequest`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | collection created | `application/json`: **Ref:** `#/components/schemas/MongoCollectionInfo`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
