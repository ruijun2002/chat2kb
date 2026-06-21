# List cluster accounts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `listAccounts`
- **Tags:** account, rdbms, shared

## Description

list accounts in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/accountList`   |
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
