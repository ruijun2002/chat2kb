# Get cluster list

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/clusters`
- **Operation ID:** `listClusters`
- **Tags:** cluster, shared

## Description

Get cluster list

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | Organization name, if envName is provided, orgName is required |
| `envName` | query | false | `string` | Environment name |
| `withStatic` | query | false | `boolean` | Whether to include static clusters |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/clusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
