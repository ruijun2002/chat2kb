# delete a existed relation between the clusters in the organization

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/relation/{target}`
- **Operation ID:** `deleteRelation`
- **Tags:** relation, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `target` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | delete a existed relation between the clusters in the organization successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
