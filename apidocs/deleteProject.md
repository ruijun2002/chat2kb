# Delete a project in an environment

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/projects/{projectName}`
- **Operation ID:** `deleteProject`
- **Tags:** project

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | environment name |
| `projectName` | path | true | `string` | project name |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | A successful response. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
