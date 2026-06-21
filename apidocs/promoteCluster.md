# Promote cluster intance to primary

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/promote`
- **Operation ID:** `promoteCluster`
- **Tags:** opsrequest, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/opsPromote`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `202` | Accepted | `application/json`: **Ref:** `#/components/schemas/opsRequestName`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
