# Update the resource quota of an organization

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/resourceQuota`
- **Operation ID:** `resourceQuota`
- **Tags:** organizationResourceQuota

## Description

Update the resource quota of an organization

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/orgResourceQuota`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `401` |  |  |
| `403` |  |  |
