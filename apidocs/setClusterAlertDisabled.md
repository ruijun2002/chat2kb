# Set cluster alert disabled or enabled

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/alerts/cluster/{clusterName}`
- **Operation ID:** `setClusterAlertDisabled`
- **Tags:** clusterAlertSwitch, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | clusterName |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/alertCluster`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertCluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
