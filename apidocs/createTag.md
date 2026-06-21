# Create cluster tags

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/tags`
- **Operation ID:** `createTag`
- **Tags:** clusterTag, shared

## Description

create tag

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/tagCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | create tag successfully | `application/json`: **Ref:** `#/components/schemas/tagCreate`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
