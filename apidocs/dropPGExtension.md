# drop PostgreSQL extension

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions/{extensionName}`
- **Operation ID:** `dropPGExtension`
- **Tags:** postgresql

## Description

drop PostgreSQL extension

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | name of the cluster |
| `extensionName` | path | true | `string` | The name of the PostgreSQL extension to uninstall. |
| `database` | query | true | `string` | The database where the extension is installed. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
