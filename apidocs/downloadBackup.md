# Download full backup

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/backups/{backupId}/download`
- **Operation ID:** `downloadBackup`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `backupId` | path | true | `string` | the id of backup |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response | `application/octet-stream`: **Type:** `string`   |
