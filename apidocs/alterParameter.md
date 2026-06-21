# alter cluster parameter

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tenant/{tenantId}/parameter`
- **Operation ID:** `alterParameter`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `tenantId` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/DmsObAlterParameter`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | close the session success | `text/plain`: **Type:** `string`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
