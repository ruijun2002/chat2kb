# Get cluster restore time ragne

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clustersWithDelete/restoreTimeRange`
- **Operation ID:** `getRestoreTimeRange`
- **Tags:** restore, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterID` | query | true | `string` | ID of the KubeBlocks cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/backup`   |
| `401` |  |  |
| `403` |  |  |
