# create inspection task by org

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/inspectionTasksByOrg`
- **Operation ID:** `createInspectionTaskByOrg`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/inspectionTask`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | No content. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
