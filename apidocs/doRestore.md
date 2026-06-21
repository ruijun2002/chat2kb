# Restore current cluster or instance

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/restore`
- **Operation ID:** `doRestore`
- **Tags:** restore, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the KubeBlocks cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/restore`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/restore`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
