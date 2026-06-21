# Delete storage class

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}`
- **Operation ID:** `deleteStorageClass`
- **Tags:** storageClass

## Description

Delete the storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |
| `storageClassName` | path | true | `string` | Name of the Storage Class to be deleted |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Successfully delete The storage class. | `*/*`: **Type:** `object` **Properties:** message   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the environment or storage class does not exist. | `*/*`: **Type:** `string`   |
