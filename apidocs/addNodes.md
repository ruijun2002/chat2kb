# Add nodes to environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/nodes`
- **Operation ID:** `addNodes`
- **Tags:** environment

## Description

Add nodes to environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/nodePool`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | environment nodepool | `application/json`: **Ref:** `#/components/schemas/nodePool`   |
| `401` |  |  |
| `403` |  |  |
