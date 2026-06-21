# get environment backup repo

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environmentBackupRepo`
- **Operation ID:** `getEnvironmentBackupRepo`
- **Tags:** environment

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentBackupRepo`   |
| `403` |  |  |
| `404` |  |  |
