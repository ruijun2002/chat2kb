# Delete backup

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/backups/{backupId}`
- **Operation ID:** `deleteBackup`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `backupId` | path | true | `string` | id of the Backup |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
