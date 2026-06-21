# get backup method

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/{engineName}/clusterBackupMethod`
- **Operation ID:** `getBackupMethod`
- **Tags:** backupMethod, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `engineName` | path | true | `string` | engine name |
| `clusterID` | query | false | `string` | clusterID is required when you want to get the backup method of a existing cluster |
| `enablePITR` | query | false | `boolean` | define whether to enable PITR (Point-In-Time Recovery). This setting is required when clusterId is not empty. |
| `withRebuildInstance` | query | false | `boolean` | defined whether to search for rebuilding instance. |
| `withRestoreCluster` | query | false | `boolean` | defined whether to search for restoring cluster. |
| `withHScale` | query | false | `boolean` | defined whether to search for rebuilding instance. |
| `component` | query | false | `string` | The component type is required when withRebuildInstance/withHScale is true. |
| `mode` | query | false | `string` | The cluster mode, used to filter out unsupported backup methods. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `*/*`: **Ref:** `#/components/schemas/clusterBackupMethod`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
