# Update cluster specified fields

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}`
- **Operation ID:** `patchCluster`
- **Tags:** cluster, shared

## Description

Update the specified Cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/clusterUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when project is updated successfully. | `application/json`: **Ref:** `#/components/schemas/cluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
