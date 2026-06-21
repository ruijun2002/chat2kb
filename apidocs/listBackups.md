# List backups

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/backups`
- **Operation ID:** `listBackups`
- **Tags:** backup

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | name of the Org |
| `clusterName` | query | false | `string` | cluster name of the Backup |
| `clusterID` | query | false | `string` | cluster ID of the Backup |
| `backupRepo` | query | false | `string` | backup repo of the Backup |
| `fetchWithDeletedCluster` | query | false | `boolean` | defined whether to search for deleted clusters. if not set, returns all backups |
| `withDeletedBackups` | query | false | `boolean` | defined whether to search for deleted backups. if not set, only return backups that are not deleted |
| `withRestoreCluster` | query | false | `boolean` | defined whether to search for restore backups. |
| `backupType` | query | false | `string` | type of the backup |
| `componentName` | query | false | `string` | get the backups belong to the component |
| `page` | query | false | `integer` | page number |
| `pageSize` | query | false | `integer` | page size |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupList`   |
| `401` |  |  |
| `403` |  |  |
