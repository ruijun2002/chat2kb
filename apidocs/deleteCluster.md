# Delete cluster

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}`
- **Operation ID:** `deleteCluster`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `force` | query | false | `boolean` | if it is true, the cluster will be deleted no matter what the termination policy is, and will not be moved to the recycle bin. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
