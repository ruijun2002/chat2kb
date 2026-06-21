# List Kubernetes nodes

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/kubernetes/nodes`
- **Operation ID:** `listKubernetesNode`
- **Tags:** environment

## Description

List Kubernetes nodes before registered as environment

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `region` | query | false | `string` | region of Kubernetes node |
| `zone` | query | false | `string` | zone of Kubernetes node |
| `op` | query | false | `#/components/schemas/listKubernetesNodeOpType` | operation of this query, either in or notin |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/kubeconfig`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/nodeList`   |
| `403` |  |  |
| `404` |  |  |
