# list MongoDB databases

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/databases`
- **Operation ID:** `listMongoDatabases`
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

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Type:** `string`   |
