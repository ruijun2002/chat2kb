# Delete a cloud provider

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/providers/{providerName}`
- **Operation ID:** `deleteCloudProvider`
- **Tags:** provider

## Description

Delete a cloud provider

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `providerName` | path | true | `string` | Name of the cloud provider |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
