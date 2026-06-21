# Update backup policy

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupPolicy`
- **Operation ID:** `updateBackupPolicy`
- **Tags:** backup, shared

## Description

partially update the specified Backup Policy

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `useVolumeSnapshot` | query | false | `boolean` | use volume snapshot to back up |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupPolicy`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when project is deleted successfully. | `application/json`: **Ref:** `#/components/schemas/backupPolicy`   |
| `401` |  |  |
