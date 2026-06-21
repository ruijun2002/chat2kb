# Restore cluster from the Recycle Bin of the Org

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}/restore`
- **Operation ID:** `restoreRecycleBinCluster`
- **Tags:** recycleBinCluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/cluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
