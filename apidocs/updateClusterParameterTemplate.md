# Update cluster parameter template

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate`
- **Operation ID:** `updateClusterParameterTemplate`
- **Tags:** parameterTemplate, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/paramTpls`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | update cluster parameter template successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
