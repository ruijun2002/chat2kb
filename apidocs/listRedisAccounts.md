# list redis accounts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/redis/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `listRedisAccounts`
- **Tags:** redis, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | the name of organization |
| `clusterName` | path | true | `string` | the name of cluster |
| `component` | query | false | `string` | the component type to list accounts |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list redis users success | `application/json`: **Ref:** `#/components/schemas/ACLUserResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
