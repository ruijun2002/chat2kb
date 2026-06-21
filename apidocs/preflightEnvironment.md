# Preflight check before create Environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/preflight`
- **Operation ID:** `preflightEnvironment`
- **Tags:** environment

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/preflightList`   |
