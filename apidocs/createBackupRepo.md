# Create backup repo

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/backupRepo`
- **Operation ID:** `createBackupRepo`
- **Tags:** backupRepo

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupRepoCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupRepo`   |
| `201` | Returned when edge is created successfully. | `application/json`: **Ref:** `#/components/schemas/backupRepo`   |
| `401` |  |  |
| `403` |  |  |
