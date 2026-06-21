# delete mssql account compatible with windows account

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/mssql/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `deleteMssqlAccount`
- **Tags:** account, mssql, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |
| `account` | query | true | `string` | name of the account |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
