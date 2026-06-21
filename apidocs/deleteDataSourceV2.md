# delete the datasource

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}`
- **Operation ID:** `deleteDataSourceV2`
- **Tags:** dms, shared

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
| `204` | Returned when datasource is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
