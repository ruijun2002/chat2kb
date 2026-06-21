# Get Kubernetes DNS

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/kubernetes/dns`
- **Operation ID:** `getKubernetesDNS`
- **Tags:** environment

## Description

Get Kubernetes DNS

## Parameters

_No parameters._

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/dns`   |
| `403` |  |  |
| `404` |  |  |
