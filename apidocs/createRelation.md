# create a relation between the clusters in the organization

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/relations`
- **Operation ID:** `createRelation`
- **Tags:** relation, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `target` | query | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | create a relation between the clusters in the organization successfully |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
