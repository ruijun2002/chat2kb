# create storage class

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses`
- **Operation ID:** `createStorageClass`
- **Tags:** storageClass

## Description

Create storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/storageClassCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully create the storage class. | `*/*`: **Ref:** `#/components/schemas/storageClassInfo`   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the resource does not exist. | `*/*`: **Type:** `string`   |
