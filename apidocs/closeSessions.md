# close the session for the cluster

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/session/{session}`
- **Operation ID:** `closeSessions`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `session` | path | true | `string` | name of the storage volume |
| `keep` | query | false | `string` | whether only close the query and keep the session |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | close the session success | `text/plain`: **Type:** `string`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
