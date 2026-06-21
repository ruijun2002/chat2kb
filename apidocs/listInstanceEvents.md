# List instance events

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/instances/{instanceName}/events`
- **Operation ID:** `listInstanceEvents`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |
| `instanceName` | path | true | `string` | name of the instance |
| `returnNumber` | query | false | `integer` | return number of events |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/instanceEventList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
