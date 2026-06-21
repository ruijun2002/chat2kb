# Create a project in an environment

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/projects`
- **Operation ID:** `createProject`
- **Tags:** project

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/projectCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | A successful response. | `application/json`: **Ref:** `#/components/schemas/project`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
