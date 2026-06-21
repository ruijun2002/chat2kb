# Create cluster database

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/databases`
- **Operation ID:** `createDatabase`
- **Tags:** database, rdbms, shared

## Description

create a database in cluster

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/database`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when database is created successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
