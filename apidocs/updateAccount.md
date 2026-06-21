# update cluster account

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `updateAccount`
- **Tags:** account, rdbms, shared

## Description

update an account in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |
| `accountName` | path | true | `string` | name of the account |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/account`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Update account password successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
