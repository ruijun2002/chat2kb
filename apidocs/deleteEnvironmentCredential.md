# Delete environment credential

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/credentials/{credentialName}`
- **Operation ID:** `deleteEnvironmentCredential`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `credentialName` | path | true | `string` | name of the environment credential |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when environment credential is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
