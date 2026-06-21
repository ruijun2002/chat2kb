# List tags by organization name

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/tags`
- **Operation ID:** `listOrgTags`
- **Tags:** clusterTag, shared

## Description

List tags by organization name.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list tags successfully | `application/json`: **Ref:** `#/components/schemas/orgTagsList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
