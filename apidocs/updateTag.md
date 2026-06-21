# updateTag

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/organizations/{orgName}/tags/{tagId}`
- **Operation ID:** `updateTag`
- **Tags:** clusterTag, shared

## Description

Update cluster tags

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `tagId` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/tagUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/tag`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
