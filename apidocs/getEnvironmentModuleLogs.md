# Get logs for an environment module pod. When no parameters other than containerName and search are provided, start streaming logs in real-time.

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/modules/{moduleName}/pods/{podName}/logs`
- **Operation ID:** `getEnvironmentModuleLogs`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Environment Name |
| `moduleName` | path | true | `string` | Environment module name |
| `podName` | path | true | `string` | Pod name |
| `containerName` | query | false | `string` | Container name |
| `sinceSeconds` | query | false | `integer` | Get logs from the last n seconds |
| `sinceTime` | query | false | `string` | Get logs since this time (RFC3339 format) |
| `tailLines` | query | false | `integer` | Number of lines to return from the end |
| `search` | query | false | `string` | Search keyword in logs |
| `previous` | query | false | `boolean` | Get previous terminated container logs |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Success | `application/json`: **Ref:** `#/components/schemas/environmentModuleLogs`   |
| `400` |  |  |
| `404` |  |  |
| `500` |  |  |
