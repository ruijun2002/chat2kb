# Update a cloud provider

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/providers/{providerName}`
- **Operation ID:** `updateCloudProvider`
- **Tags:** provider

## Description

Update a cloud provider

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `providerName` | path | true | `string` | Name of the cloud provider |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/providerUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/provider`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
