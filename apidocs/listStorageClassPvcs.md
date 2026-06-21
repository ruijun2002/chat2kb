# get persistentvolumeclaim list of the storage class

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/storageClasses/{storageClassName}/pvcs`
- **Operation ID:** `listStorageClassPvcs`
- **Tags:** storageClass

## Description

get the persistentvolumeclaim list related to the specified storage class for the specified environment.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | Name of the Environment |
| `storageClassName` | path | true | `string` | Name of the Storage Class to be specified |
| `node` | query | false | `string` | Name of the Node to be specified |
| `orgName` | query | false | `string` | Name of the Org to be specified |
| `clusterName` | query | false | `string` | Name of the Cluster to be specified |
| `pageId` | query | true | `integer` | defined page id. |
| `pageSize` | query | true | `integer` | defined page size. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successfully get the  storage class. | `*/*`: **Ref:** `#/components/schemas/persistentVolumeClaimList`   |
| `403` | Returned when the user does not have permission to access the resource. | `*/*`: **Type:** `object`   |
| `404` | Returned when the environment or persistentvolumeclaim does not exist. | `*/*`: **Type:** `string`   |
