# Delete an engine license entity by ID

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/engineLicenseEntity`
- **Operation ID:** `deleteEngineLicenseEntity`
- **Tags:** engine

## Description

delete an engine license entity by ID

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `entityId` | query | true | `string` | entity ID |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | No Content |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
