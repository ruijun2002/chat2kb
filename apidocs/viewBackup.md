# view backup info

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/backups/{backupId}/view`
- **Operation ID:** `viewBackup`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `backupId` | path | true | `string` | the id of backup |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupView`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `*/*`: **Ref:** `#/components/schemas/fileEntryList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
