# Delete backup repo

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}`
- **Operation ID:** `deleteBackupRepo`
- **Tags:** backupRepo

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `backupRepoName` | path | true | `string` | name of the BackupRepo |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
