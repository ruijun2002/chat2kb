# Create image registry

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/imageRegistries`
- **Operation ID:** `createImageRegistry`
- **Tags:** imageRegistry

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/imageRegistry`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when image registry is created successfully. | `application/json`: **Ref:** `#/components/schemas/imageRegistry`   |
