# Get organization

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}`
- **Operation ID:** `readOrg`
- **Tags:** organization, shared

## Description

read the specified Org

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/org`   |
| `401` |  |  |
| `403` |  |  |
