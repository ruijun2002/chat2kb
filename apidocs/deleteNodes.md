# Delete nodes from environment

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/nodes`
- **Operation ID:** `deleteNodes`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Type:** `array` **Items:** **Type:** `string`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when nodes are deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
