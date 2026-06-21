# Get cluster details by ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clustersWithDelete/{clusterID}`
- **Operation ID:** `getClusterByID`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterID` | path | true | `string` | ID of the KubeBlocks cluster |
| `backupName` | query | false | `string` | Backup name to override cluster components from its snapshot |
| `restoreTime` | query | false | `string` | Restore time to find latest continuous backup snapshot after this time |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/cluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
