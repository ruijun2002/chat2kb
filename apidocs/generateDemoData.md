# generate demo data

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/{engineName}/organizations/{orgName}/clusters/{clusterName}/demo`
- **Operation ID:** `generateDemoData`
- **Tags:** rdbms, shared

## Description

generate demo data

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `engineName` | path | true | `string` | name of the engine |
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | query | true | `string` | acccount name which owns the database to generate demo data |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when demo data is generated successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
