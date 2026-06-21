# Create backup

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/backups`
- **Operation ID:** `createClusterBackup`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `component` | query | false | `string` | name of the component |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/backupCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backup`   |
| `401` |  |  |
| `403` |  |  |
