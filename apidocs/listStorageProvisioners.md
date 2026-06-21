# List the provisioners that can be used by storage class of a environment

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storageProvisioners`
- **Operation ID:** `listStorageProvisioners`
- **Tags:** storageClass

## Description

Provides a summary of storage provisioners statistics.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the Environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `*/*`: **Ref:** `#/components/schemas/storageProvisionerList`   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the resource does not exist. | `*/*`: **Type:** `string`   |
