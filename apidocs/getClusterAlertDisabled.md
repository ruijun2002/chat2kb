# Check if cluster alert is disabled

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/alerts/cluster/{clusterName}`
- **Operation ID:** `getClusterAlertDisabled`
- **Tags:** clusterAlertSwitch, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | clusterName |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/alertCluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
