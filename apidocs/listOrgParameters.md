# List parameters of an organization

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/parameters`
- **Operation ID:** `listOrgParameters`
- **Tags:** organizationParameter, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |
| `category` | query | false | `string` | the category of the parameters |
| `name` | query | false | `string` | the name of the parameter |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgParameterList`   |
| `401` |  |  |
| `403` |  |  |
