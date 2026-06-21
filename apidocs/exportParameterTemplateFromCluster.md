# Export parameter template from cluster

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/parameterTemplate`
- **Operation ID:** `exportParameterTemplateFromCluster`
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
**Ref:** `#/components/schemas/paramTplCreateFromCluster`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | export parameter template from cluster successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
