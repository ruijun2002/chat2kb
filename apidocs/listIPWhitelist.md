# List IP whitelists

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist`
- **Operation ID:** `listIPWhitelist`
- **Tags:** ipWhitelist, shared

## Description

_No description provided._

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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/ipWhitelistList`   |
| `403` |  |  |
| `404` |  |  |
