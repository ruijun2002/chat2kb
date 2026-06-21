# Get cloud provider

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/providers/{providerName}`
- **Operation ID:** `getCloudProvider`
- **Tags:** provider

## Description

Get cloud provider

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `providerName` | path | true | `string` | Name of the cloud provider |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/provider`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
