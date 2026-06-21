# create inspection task by env

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/inspectionTasksByEnv`
- **Operation ID:** `createInspectionTaskByEnv`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/inspectionTask`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | No content. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
