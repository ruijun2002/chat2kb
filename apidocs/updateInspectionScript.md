# Update inspection script

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/inspectionScripts/{scriptId}`
- **Operation ID:** `updateInspectionScript`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `scriptId` | path | true | `string` | id of the inspection script |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/inspectionScript`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/inspectionScript`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
