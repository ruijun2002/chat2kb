# Disable service version

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engineVersions/disable`
- **Operation ID:** `disableServiceVersion`
- **Tags:** engine

## Description

Remove a service version from the engine version's service_versions list if no running clusters are using it

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/engineVersionDisableServiceVersion`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineVersion`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
