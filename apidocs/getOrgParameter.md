# Get a parameter of an organization

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/parameters/{parameterName}`
- **Operation ID:** `getOrgParameter`
- **Tags:** organizationParameter, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |
| `parameterName` | path | true | `string` | The name of the parameter |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgParameter`   |
| `401` |  |  |
| `403` |  |  |
