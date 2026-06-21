# Delete organization

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}`
- **Operation ID:** `deleteOrg`
- **Tags:** organization, shared

## Description

partially delete the specified org

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when org is deleted successfully. |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
