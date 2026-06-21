# Produce message to topic

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages`
- **Operation ID:** `produceKafkaTopicMessage`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `topic` | path | true | `string` |  |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/TopicMessageRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Type:** `integer` 生成消息的字节长度   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
