# list all tenants for the oceanbase cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenants`
- **Operation ID:** `listTenants`
- **Tags:** oceanbase, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/TenantList`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
