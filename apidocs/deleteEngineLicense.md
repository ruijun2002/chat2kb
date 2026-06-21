# Delete engine license

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/engineLicense`
- **Operation ID:** `deleteEngineLicense`
- **Tags:** engineLicense

## Description

delete an engine license

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `licenseId` | query | true | `string` | license id |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
