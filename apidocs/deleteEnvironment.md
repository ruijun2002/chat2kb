# Delete environment

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}`
- **Operation ID:** `deleteEnvironment`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentDelete`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
