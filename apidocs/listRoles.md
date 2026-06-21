# List roles of a organization

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/roles`
- **Operation ID:** `listRoles`
- **Tags:** role, shared

## Description

List roles of a organization

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/roleList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
