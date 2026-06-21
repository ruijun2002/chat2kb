# Create a cloud provider

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/providers`
- **Operation ID:** `createCloudProvider`
- **Tags:** provider

## Description

Create a cloud provider

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/providerCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Created | `application/json`: **Ref:** `#/components/schemas/provider`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
