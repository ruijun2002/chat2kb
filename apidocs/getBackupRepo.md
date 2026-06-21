# Get backup repo

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}`
- **Operation ID:** `getBackupRepo`
- **Tags:** backupRepo, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `backupRepoName` | path | true | `string` | name of the BackupRepo |
| `orgName` | query | false | `string` | name of the organization |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupRepo`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
