# list all session for the cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/sessions`
- **Operation ID:** `listSessionsOld`
- **Tags:** dms, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |
| `all` | query | false | `string` | whether list all session includes sleep |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list all session success | `application/json`: **Ref:** `#/components/schemas/DmsSessionList`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
