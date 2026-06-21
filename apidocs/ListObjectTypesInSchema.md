# list the type and number of database objects in the specified database or schema

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/{schema}`
- **Operation ID:** `ListObjectTypesInSchema`
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
| `database` | query | false | `string` | database name, used by engines such as MSSQL when listing objects inside a schema |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/DmsObjectList`   |
