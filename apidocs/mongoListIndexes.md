# list MongoDB collection indexes

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/indexes`
- **Operation ID:** `mongoListIndexes`
- **Tags:** dms

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `id` | path | true | `string` |  |
| `db` | path | true | `string` |  |
| `col` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/MongoIndexInfo`   |
