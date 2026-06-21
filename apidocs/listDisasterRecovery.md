# List Disaster Recovery instances under the main cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/parent/{parentClusterID}/disasterRecovery`
- **Operation ID:** `listDisasterRecovery`
- **Tags:** disasterRecovery

## Description

Retrieve a list of disaster recovery instances for a specific database cluster.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `parentClusterID` | path | true | `string` | The ID of the parent database cluster |
| `orgName` | path | true | `string` | name of the org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A list of disaster recovery instances. | `application/json`: **Ref:** `#/components/schemas/disasterRecoveryClusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
