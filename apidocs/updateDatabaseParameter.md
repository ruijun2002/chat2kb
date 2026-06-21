# Update database parameter

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/databaseParameters`
- **Operation ID:** `updateDatabaseParameter`
- **Tags:** databaseParameters

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/databaseParameterItem`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | update database parameter successfully | `application/json`: **Ref:** `#/components/schemas/databaseParameterItem`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
