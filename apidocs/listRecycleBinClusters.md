# List all clusters in the Recycle Bin

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/recycleBin/clusters`
- **Operation ID:** `listRecycleBinClusters`
- **Tags:** recycleBinCluster

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/recycleBinClusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
