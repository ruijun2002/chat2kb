# Get the resource quota and usage of an organization

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/resourceQuota`
- **Operation ID:** `resourceQuotaAndUsage`
- **Tags:** organizationResourceQuota

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of the organization |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/orgResourceQuotaAndUsage`   |
| `401` |  |  |
| `403` |  |  |
