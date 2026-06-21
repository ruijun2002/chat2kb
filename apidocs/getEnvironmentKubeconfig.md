# Get environment kubeconfig

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/kubeconfig`
- **Operation ID:** `getEnvironmentKubeconfig`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/httpBody`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
