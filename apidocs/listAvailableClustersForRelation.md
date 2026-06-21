# list the available clusters for the organization to create the a relation

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/cluster/{clusterName}/available-relations`
- **Operation ID:** `listAvailableClustersForRelation`
- **Tags:** relation, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `targetType` | query | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list the available clusters for the organization to create the a relation successfully | `application/json`: **Ref:** `#/components/schemas/availableClusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
