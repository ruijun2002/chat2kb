# List consumer offsets of topic

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/consumer-groups/{groupId}/offsets`
- **Operation ID:** `listKafkaTopicConsumerOffsets`
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

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/TopicOffsetList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
