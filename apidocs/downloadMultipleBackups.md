# Download multiple backup files

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/backups/{backupId}/download`
- **Operation ID:** `downloadMultipleBackups`
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
**Ref:** `#/components/schemas/backupDownload`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response | `application/octet-stream`: **Type:** `string`   |
