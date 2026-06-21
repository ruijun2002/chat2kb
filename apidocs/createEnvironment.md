# Create environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments`
- **Operation ID:** `createEnvironment`
- **Tags:** environment

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when environment is created successfully. | `application/json`: **Ref:** `#/components/schemas/environment`   |
| `403` |  |  |
| `404` |  |  |
