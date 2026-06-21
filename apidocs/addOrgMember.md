# Add member

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/members`
- **Operation ID:** `addOrgMember`
- **Tags:** member, shared

## Description

Add organization with specific role

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgMemberAdd`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgMember`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
