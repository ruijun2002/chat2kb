# List environments

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments`
- **Operation ID:** `listEnvironment`
- **Tags:** environment

## Description

List environments

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | name of the Org |
| `cloudProvider` | query | false | `string` | cloud provider of the Environment |
| `cloudRegion` | query | false | `string` | cloud region of the Environment |
| `environmentType` | query | false | `#/components/schemas/environmentType` | type of the Environment |
| `engine` | query | false | `string` | engine name |
| `version` | query | false | `string` | version of the engine |
| `slaEnabled` | query | false | `boolean` | whether the environment is enabled for SLA |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/environmentList`   |
| `403` |  |  |
| `404` |  |  |
