# Update environment credential

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/credentials/{credentialName}`
- **Operation ID:** `patchEnvironmentCredential`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `credentialName` | path | true | `string` | name of the environment credential |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentCredentialUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/environmentCredential`   |
| `401` |  |  |
| `403` |  |  |
