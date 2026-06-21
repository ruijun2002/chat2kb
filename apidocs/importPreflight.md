# Data source preflight check

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/import/preflight`
- **Operation ID:** `importPreflight`
- **Tags:** import, shared

## Description

Initiates async validation with the selected source configuration

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Organization name |
| `clusterName` | path | true | `string` | Cluster name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ImportPreflightRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Preflight initiated successfully, returns task ID for querying results | `application/json`: **Ref:** `#/components/schemas/preCheckTaskResponse`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
