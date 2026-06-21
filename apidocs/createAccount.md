# Create cluster account

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `createAccount`
- **Tags:** account, rdbms, shared

## Description

create an account in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the organization |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/account`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | create redis account success | `application/json`: **Ref:** `#/components/schemas/account`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
