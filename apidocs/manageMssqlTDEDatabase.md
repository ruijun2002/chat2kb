# batch modify database tde status

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/tde`
- **Operation ID:** `manageMssqlTDEDatabase`
- **Tags:** mssql, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/dbTDERequest`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Enable mssql database in tde successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
