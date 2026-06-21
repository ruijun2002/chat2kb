# get restore workload logs of the cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/restore/{restoreId}/logs`
- **Operation ID:** `GetRestoreLog`
- **Tags:** restore, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `restoreId` | path | true | `string` | id of the restore |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/restoreLog`   |
| `401` |  |  |
| `403` |  |  |
