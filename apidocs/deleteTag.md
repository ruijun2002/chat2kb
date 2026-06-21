# Delete tag

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/tags/{tagId}`
- **Operation ID:** `deleteTag`
- **Tags:** clusterTag, shared

## Description

delete cluster tag

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `tagId` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
