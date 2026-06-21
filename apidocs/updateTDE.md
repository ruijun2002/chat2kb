# Enable TDE

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tde`
- **Operation ID:** `updateTDE`
- **Tags:** cluster, shared

## Description

Enable transparent data encryption for a cluster component. Disabling TDE is not supported.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/tdeRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/tdeResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
