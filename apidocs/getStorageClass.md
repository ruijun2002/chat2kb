# get storage class

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}`
- **Operation ID:** `getStorageClass`
- **Tags:** storageClass

## Description

get the storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |
| `storageClassName` | path | true | `string` | Name of the Storage Class to be updated |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully get the  storage class. | `*/*`: **Ref:** `#/components/schemas/storageClassInfo`   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the environment or storage class does not exist. | `*/*`: **Type:** `string`   |
