# Update backup schedule

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backupSchedules/{scheduleName}`
- **Operation ID:** `updateBackupSchedule`
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

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupScheduleUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupSchedule`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
