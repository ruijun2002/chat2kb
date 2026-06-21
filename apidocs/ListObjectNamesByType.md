# list the all name for the specified object type

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}/{type}`
- **Operation ID:** `ListObjectNamesByType`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |
| `schema` | path | true | `string` | schema or database name |
| `type` | path | true | `string` | object type |
| `database` | query | false | `string` | database name, used by engines such as MSSQL when listing object names inside a schema |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/DmsObjectNameList`   |
