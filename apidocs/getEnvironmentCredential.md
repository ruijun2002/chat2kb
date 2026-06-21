# Get environment credential

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/credentials/{credentialName}`
- **Operation ID:** `getEnvironmentCredential`
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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentCredential`   |
| `403` |  |  |
| `404` |  |  |
