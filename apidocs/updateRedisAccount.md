# update redis account

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `updateRedisAccount`
- **Tags:** redis, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | the name of organization |
| `clusterName` | path | true | `string` | the name of cluster |
| `accountName` | path | true | `string` | the name of account |
| `component` | query | false | `string` | in which component type to update account |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ACLUser`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | update redis account success | `application/json`: **Ref:** `#/components/schemas/opsRequestName`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
