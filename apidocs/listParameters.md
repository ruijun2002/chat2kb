# list cluster parameters

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameters`
- **Operation ID:** `listParameters`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `tenantId` | path | true | `string` |  |
| `mode` | query | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/DmsParameterList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
