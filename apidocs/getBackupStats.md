# Get backup statistics

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/backupStats`
- **Operation ID:** `getBackupStats`
- **Tags:** backup

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | name of the Org |
| `clusterID` | query | false | `string` | id of the Cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backupStats`   |
| `401` |  |  |
| `403` |  |  |
