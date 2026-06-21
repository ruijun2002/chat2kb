# Create a new disaster recovery instance

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/parent/{parentClusterID}/disasterRecovery`
- **Operation ID:** `createDisasterRecovery`
- **Tags:** disasterRecovery

## Description

Create a new disaster recovery instance for a database cluster.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `parentClusterID` | path | true | `string` | The ID of the parent database cluster |
| `orgName` | path | true | `string` | name of the org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/disasterRecoveryCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Disaster recovery instance async job task information. | `application/json`: **Ref:** `#/components/schemas/disasterRecoveryTask`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
