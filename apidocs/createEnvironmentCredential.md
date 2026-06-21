# Create environment credential

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/credentials`
- **Operation ID:** `createEnvironmentCredential`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/environmentCredentialCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when environment credential is created successfully. | `application/json`: **Ref:** `#/components/schemas/environmentCredential`   |
| `403` |  |  |
| `404` |  |  |
