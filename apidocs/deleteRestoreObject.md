# Delete restore task

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/restore`
- **Operation ID:** `deleteRestoreObject`
- **Tags:** restore, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `restoreName` | query | true | `string` | name of the restore |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
