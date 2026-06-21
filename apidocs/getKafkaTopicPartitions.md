# Get partition list of topic

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/partitions`
- **Operation ID:** `getKafkaTopicPartitions`
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

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/PartitionList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
