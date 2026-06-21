# list collections in a MongoDB database

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections`
- **Operation ID:** `listMongoCollections`
- **Tags:** dms

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |
| `db` | path | true | `string` | database name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/MongoCollectionInfo`   |
