# Delete mongodb account

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/mongodb/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `deleteMongoDBAccount`
- **Tags:** account, mongodb, shared

## Description

delete an account in mongodb

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | path | true | `string` | name of the Cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
