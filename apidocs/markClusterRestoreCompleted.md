# mark cluster to restore completed, usually used when manually repairing or recovering issues

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/markClusterRestoreCompleted`
- **Operation ID:** `markClusterRestoreCompleted`
- **Tags:** markCluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
