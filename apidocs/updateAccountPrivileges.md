# update account privileges

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}/privileges`
- **Operation ID:** `updateAccountPrivileges`
- **Tags:** account, rdbms, shared

## Description

update account privileges for rdbms engine

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | path | true | `string` | name of the account |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/privilegeList`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when account privileges are updated successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
