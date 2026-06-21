# Create engine resource constraint

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/engines/resourceConstraints`
- **Operation ID:** `createEngineResourceConstraint`
- **Tags:** engine

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/resourceConstraintCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | OK | `application/json`: **Ref:** `#/components/schemas/resourceConstraint`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
