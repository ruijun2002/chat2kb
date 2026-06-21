# Lock cluster account

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}/lock`
- **Operation ID:** `lockAccount`
- **Tags:** account, rdbms, shared

## Description

lock an account in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |
| `accountName` | path | true | `string` | name of the account |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when account is locked successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
