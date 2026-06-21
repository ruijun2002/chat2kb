# Create database parameter

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/databaseParameters`
- **Operation ID:** `createDatabaseParameter`
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
| `200` | create database parameter successfully | `application/json`: **Ref:** `#/components/schemas/databaseParameterItem`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
