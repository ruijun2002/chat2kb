# Update backup repo

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}`
- **Operation ID:** `updateBackupRepo`
- **Tags:** backupRepo

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `backupRepoName` | path | true | `string` | name of the BackupRepo |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupRepoUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupRepo`   |
| `401` |  |  |
| `403` |  |  |
