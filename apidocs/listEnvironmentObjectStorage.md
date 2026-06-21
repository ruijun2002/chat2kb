# List environment object storage

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environmentObjectStorage`
- **Operation ID:** `listEnvironmentObjectStorage`
- **Tags:** environment

## Description

List environment object storage

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentObjectStorage`   |
| `403` |  |  |
| `404` |  |  |
