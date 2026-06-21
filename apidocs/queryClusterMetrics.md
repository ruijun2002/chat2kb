# Query cluster metrics

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/metrics`
- **Operation ID:** `queryClusterMetrics`
- **Tags:** cluster, shared

## Description

Query cluster metrics by specified metric name and instance name, support instant and range query

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `query` | query | true | `string` | The promQL query string |
| `queryType` | query | true | `#/components/schemas/metricsQueryType` | The query type in the query, if use instant, the query will return the lastest instant value, if use range, the query will return a list of values in the time range |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/clusterMetrics`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
