# get tenants detail information of the oceanbase cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}`
- **Operation ID:** `getTenant`
- **Tags:** oceanbase, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `tenantId` | path | true | `string` | id of the tenant |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/Tenant`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
