# Get cluster tags

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusterTags`
- **Operation ID:** `getTags`
- **Tags:** clusterTag, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterIds` | query | true | `string` | Comma-separated list of cluster IDs |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | list tags successfully | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/clusterTags`   |
