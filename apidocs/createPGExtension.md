# create PostgreSQL extension

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/postgresql/organizations/{orgName}/clusters/{clusterName}/extensions`
- **Operation ID:** `createPGExtension`
- **Tags:** postgresql

## Description

create PostgreSQL extension

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/PgCreateExtensionOpt`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/createPgExtensionResp`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
