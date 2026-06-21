# Enable or disable cluster TLS

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/tls`
- **Operation ID:** `tlsSwitcher`
- **Tags:** tls, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/tlsRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `409` |  |  |
