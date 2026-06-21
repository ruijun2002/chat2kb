# Batch update clusters

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/clusters/batch`
- **Operation ID:** `batchUpdateClustersGlobal`
- **Tags:** cluster

## Description

Update multiple clusters with the same update information (displayName and/or maintainceWindow) in a single request

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/clusterBatchUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when clusters are updated successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
