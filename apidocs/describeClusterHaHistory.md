# describe cluster HA history

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/haHistory`
- **Operation ID:** `describeClusterHaHistory`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `componentName` | query | false | `string` | name of the component |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Accepted | `application/json`: **Ref:** `#/components/schemas/haHistoryList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
