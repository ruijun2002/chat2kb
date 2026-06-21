# Validate cluster creation

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/validate`
- **Operation ID:** `validateClusterCreation`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/clusterCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Return when cluster creation is validated successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
