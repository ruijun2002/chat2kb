# Restore new cluster

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/restore`
- **Operation ID:** `restoreCluster`
- **Tags:** restore

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/restoreCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/cluster`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
