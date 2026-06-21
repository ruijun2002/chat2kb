# List objects tree for selective backup

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/listObjectsForSelectiveBackup`
- **Operation ID:** `listObjectsTreeForSelectiveBackup`
- **Tags:** backup, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the org |
| `clusterName` | path | true | `string` | name of the cluster |
| `database` | query | false | `string` | database name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `*/*`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/selectiveObjectTreeNode`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
