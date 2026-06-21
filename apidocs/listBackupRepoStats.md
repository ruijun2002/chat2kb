# list backup repo stats

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo/{backupRepoName}/stats`
- **Operation ID:** `listBackupRepoStats`
- **Tags:** backupRepo

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `backupRepoName` | path | true | `string` | name of the environment |
| `start` | query | false | `string` | the start time |
| `end` | query | false | `string` | the end time |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupRepoStatsList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
