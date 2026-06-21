# Get cluster in the Recycle Bin of the Org

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/recycleBin/clusters/{clusterName}`
- **Operation ID:** `getRecycleBinCluster`
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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/recycleBinCluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
