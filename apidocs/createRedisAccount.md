# create redis account

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `createRedisAccount`
- **Tags:** redis, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | the name of organization |
| `clusterName` | path | true | `string` | the name of cluster |
| `component` | query | false | `string` | the component type to create account |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ACLUser`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | create redis account success | `application/json`: **Ref:** `#/components/schemas/opsRequestName`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
