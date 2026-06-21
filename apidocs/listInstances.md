# List cluster instances

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/instances`
- **Operation ID:** `listInstances`
- **Tags:** instance

## Description

List instances based on query parameters with constraints.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `envName` | query | false | `string` | Name of the environment (optional, required when querying by nodeName). |
| `nodeName` | query | false | `string` | Name of the node (optional, required when querying by envName). |
| `orgName` | query | false | `string` | Name of the organization (optional, required when querying by clusterName). |
| `clusterName` | query | false | `string` | Name of the cluster (optional). |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/instanceList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
