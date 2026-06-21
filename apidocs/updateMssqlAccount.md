# update mssql account compatible with windows account

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `updateMssqlAccount`
- **Tags:** account, mssql, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/account`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Update mssql account successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
