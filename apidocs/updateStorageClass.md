# Update storage class

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}`
- **Operation ID:** `updateStorageClass`
- **Tags:** storageClass

## Description

Updates the  storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |
| `storageClassName` | path | true | `string` | Name of the Storage Class to be updated |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/storageClassUpdate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully set the default storage class. | `*/*`: **Type:** `object` **Properties:** message   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the environment or storage class does not exist. | `*/*`: **Type:** `string`   |
