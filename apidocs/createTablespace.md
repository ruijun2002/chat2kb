# Create damengdb tablespace

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/damengdb/organizations/{orgName}/clusters/{clusterName}/tablespaces`
- **Operation ID:** `createTablespace`
- **Tags:** dameng

## Description

Create tablespace for a Dameng cluster.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/DmTablespace`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/DmTablespace`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
