# Tail cluster instance container log

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/workloads/{workloadName}/log`
- **Operation ID:** `getClusterInstanceLog`
- **Tags:** cluster, shared

## Description

read log of the specified cluster instance

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `workloadName` | path | true | `string` | name of the workload |
| `workloadType` | query | false | `string` | type of the workload, supported values ["Pod", "Job"], default value is Pod. |
| `previous` | query | false | `boolean` | Return previous terminated container logs. Defaults to false. |
| `sinceSeconds` | query | false | `integer` | A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. |
| `tailLines` | query | false | `integer` | If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `text/plain`: **Type:** `string`   |
| `401` |  |  |
