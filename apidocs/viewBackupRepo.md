# view backup repo

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/view`
- **Operation ID:** `viewBackupRepo`
- **Tags:** backupRepo

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `backupRepoName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupRepoView`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `*/*`: **Ref:** `#/components/schemas/fileEntryList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
