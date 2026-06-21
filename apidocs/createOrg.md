# Create organization

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations`
- **Operation ID:** `createOrg`
- **Tags:** organization

## Description

Create a new organization

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | OK | `application/json`: **Ref:** `#/components/schemas/org`   |
| `401` |  |  |
