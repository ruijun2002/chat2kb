# Delete member

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/members/{memberId}`
- **Operation ID:** `deleteOrgMember`
- **Tags:** member, shared

## Description

delete a Org Member

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | Name of the Org |
| `memberId` | path | true | `string` | ID of the member |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
