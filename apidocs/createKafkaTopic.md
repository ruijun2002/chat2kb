# Create new topic

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics`
- **Operation ID:** `createKafkaTopic`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/CreateTopicRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Created | `application/json`: **Ref:** `#/components/schemas/Topic`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
