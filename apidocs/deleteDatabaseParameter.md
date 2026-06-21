# Delete database parameter

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/databaseParameters`
- **Operation ID:** `deleteDatabaseParameter`
- **Tags:** databaseParameters

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/deleteDatabaseParameterItem`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when database parameter is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
