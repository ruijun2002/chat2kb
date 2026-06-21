# Reset consumer offset of topic

## Overview

- **Method:** `PUT`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets`
- **Operation ID:** `resetKafkaTopicConsumerOffset`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `topic` | path | true | `string` | The name of topic |
| `groupId` | path | true | `string` | The id of consumer group |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/ResetOffsetRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Consumer offset successfully reset |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
