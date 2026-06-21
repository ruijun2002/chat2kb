# List PostgreSQL extensions

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions`
- **Operation ID:** `listPGExtensions`
- **Tags:** postgresql

## Description

List PostgreSQL extensions

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | name of the cluster |
| `status` | query | false | `string` | extension status, if set to `installed`, only installed extensions will be returned. If not specified, all available extensions will be returned. |
| `database` | query | false | `string` | database name. This parameter is only used when status is installed; if not specified, all databases installed extensions will be returned. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/PgExtensionList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
