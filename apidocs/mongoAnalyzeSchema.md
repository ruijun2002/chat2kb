# analyze MongoDB collection schema from sample documents

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases/{db}/collections/{col}/schema`
- **Operation ID:** `mongoAnalyzeSchema`
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
| `sample` | query | false | `integer` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/MongoSchemaAnalysis`   |
