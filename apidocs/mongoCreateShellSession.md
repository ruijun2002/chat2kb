# create MongoDB mongosh runtime session

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/shell/sessions`
- **Operation ID:** `mongoCreateShellSession`
- **Tags:** dms

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `id` | path | true | `string` | id of the datasource |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/MongoShellCreateSessionRequest`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | shell session created | `application/json`: **Ref:** `#/components/schemas/MongoShellSession`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
| `503` |  |  |
