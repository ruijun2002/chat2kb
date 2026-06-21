# List cluster sessions

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/sessions`
- **Operation ID:** `listSessions`
- **Tags:** session, rdbms, shared

## Description

list sessions in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `all` | query | false | `boolean` | whether list all session includes sleep |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list all session success | `application/json`: **Ref:** `#/components/schemas/DmsSessionList`   |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
