# Create IP whitelist

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist`
- **Operation ID:** `createIPWhitelist`
- **Tags:** ipWhitelist, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

**Content-Type:** `application/json`
**Type:** `object` whitelist **Properties:** name, description, addresses

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when object is created successfully. | `application/json`: **Ref:** `#/components/schemas/ipWhitelist`   |
| `403` |  |  |
| `404` |  |  |
