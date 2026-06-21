# Create mongodb account

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `createMongoDBAccount`
- **Tags:** account, mongodb, shared

## Description

create an account in mongodb

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

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
