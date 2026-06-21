# Update the specified engine version

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/engineVersions`
- **Operation ID:** `patchEngineVersion`
- **Tags:** engine

## Description

Update the specified engine version

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineVersionUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineVersion`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
