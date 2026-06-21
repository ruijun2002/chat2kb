# scan and import backup records from storage

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/storages/{storageName}/importbackup`
- **Operation ID:** `importBackup`
- **Tags:** storage

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `storageName` | path | true | `string` | name of the storage |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/importBackup`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupList`   |
| `401` |  |  |
| `403` |  |  |
