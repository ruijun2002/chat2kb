# List backup schedules

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules`
- **Operation ID:** `listBackupSchedules`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `clusterName` | path | true | `string` | name of the cluster |
| `backupMethod` | query | false | `string` | filter by backup method |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupScheduleList`   |
| `401` |  |  |
| `403` |  |  |
