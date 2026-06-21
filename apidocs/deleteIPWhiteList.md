# Delete IP whitelist

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/ipWhitelist/{ipWhitelistId}`
- **Operation ID:** `deleteIPWhiteList`
- **Tags:** ipWhitelist, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `ipWhitelistId` | path | true | `string` | ID of the IP whitelist |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when object is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
