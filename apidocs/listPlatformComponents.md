# List platform components

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/platformComponents`
- **Operation ID:** `listPlatformComponents`
- **Tags:** platformComponent

## Description

List platform components with monitoring and log query metadata

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/platformComponentList`   |
| `401` |  |  |
| `403` |  |  |
