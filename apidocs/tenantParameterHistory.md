# List parameters history of the Oceanbase tenant

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameterHistory`
- **Operation ID:** `tenantParameterHistory`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `tenantId` | path | true | `string` | id of the tenant |
| `parameterName` | query | false | `string` | name of the parameter |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | get parameters history of the cluster successfully | `application/json`: **Ref:** `#/components/schemas/parameterHistoryList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
