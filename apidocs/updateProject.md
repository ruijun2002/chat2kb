# Update a project in an environment

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/projects/{projectName}`
- **Operation ID:** `updateProject`
- **Tags:** project

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `projectName` | path | true | `string` | project name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/projectUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/project`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
