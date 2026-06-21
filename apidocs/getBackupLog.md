# Get backup log

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/backups/{backupId}/logs`
- **Operation ID:** `getBackupLog`
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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupLog`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
