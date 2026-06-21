# Update member role

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/members/{memberId}`
- **Operation ID:** `patchOrgMember`
- **Tags:** member, shared

## Description

Only authenticated organization admins can update the member's role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `memberId` | path | true | `string` | ID of the member |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgMemberUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgMember`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
