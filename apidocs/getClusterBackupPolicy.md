# Get backup policy

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy`
- **Operation ID:** `getClusterBackupPolicy`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `useVolumeSnapshot` | query | false | `boolean` | use volume snapshot to back up |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupPolicy`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
