# build backup object with a existing backup directory

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/organizations/{orgName}/engines/{engineName}/buildBackup`
- **Operation ID:** `buildBackupObj`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `environmentName` | path | true | `string` | name of the environment |
| `engineName` | path | true | `string` | name of the engine |

## Request Body

**Content-Type:** `application/json`
**Type:** `object` **Properties:** backupPath, backupRepoName, rootUserPassword, clusterName

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backup`   |
| `401` |  |  |
| `403` |  |  |
