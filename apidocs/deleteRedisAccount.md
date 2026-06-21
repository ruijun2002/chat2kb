# delete redis account

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `deleteRedisAccount`
- **Tags:** redis, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | the name of organization |
| `clusterName` | path | true | `string` | the name of cluster |
| `accountName` | path | true | `string` | the name of account |
| `component` | query | false | `string` | in which component type to delete account |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | delete redis account success | `application/json`: **Ref:** `#/components/schemas/opsRequestName`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
