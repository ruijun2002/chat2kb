# Get member

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/members/{memberId}`
- **Operation ID:** `readOrgMember`
- **Tags:** member, shared

## Description

read the specified OrgMember

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `memberId` | path | true | `string` | ID of the member |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgMember`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
