# List members

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/members`
- **Operation ID:** `listOrgMember`
- **Tags:** member, shared

## Description

list members of the specified Org

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgMemberList`   |
| `401` |  |  |
| `403` |  |  |
