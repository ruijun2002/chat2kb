# Delete backup schedule

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules/{scheduleName}`
- **Operation ID:** `deleteBackupSchedule`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `clusterName` | path | true | `string` | name of the cluster |
| `scheduleName` | path | true | `string` | name of the backup schedule |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when backup schedule is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
