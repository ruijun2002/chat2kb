# List environment credentials

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/credentials`
- **Operation ID:** `listEnvironmentCredential`
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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentCredentialList`   |
| `403` |  |  |
| `404` |  |  |
