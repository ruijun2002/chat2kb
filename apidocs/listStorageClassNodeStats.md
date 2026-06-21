# get node stats of the storage class

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/nodeStats`
- **Operation ID:** `listStorageClassNodeStats`
- **Tags:** storageClass

## Description

get the node stats related to the specified storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |
| `storageClassName` | path | true | `string` | Name of the Storage Class to be specified |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully get the node stats of the storage class. | `application/json`: **Ref:** `#/components/schemas/storageClassNodeStatsList`   |
| `400` |  |  |
| `403` |  |  |
| `404` |  |  |
