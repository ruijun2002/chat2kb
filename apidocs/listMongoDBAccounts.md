# List mongodb accounts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `listMongoDBAccounts`
- **Tags:** account, mongodb, shared

## Description

list accounts in mongodb

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

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
