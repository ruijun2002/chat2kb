# List Kubernetes storageclass

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/kubernetes/storageclasses`
- **Operation ID:** `listKubernetesStorageClass`
- **Tags:** environment

## Description

List Kubernetes storageclass before registered as environment

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/storageClassList`   |
| `403` |  |  |
| `404` |  |  |
