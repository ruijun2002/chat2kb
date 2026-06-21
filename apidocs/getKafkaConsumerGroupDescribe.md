# Get consumer group describe

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/consumer-groups/{groupId}`
- **Operation ID:** `getKafkaConsumerGroupDescribe`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `groupId` | path | true | `string` | The id of consumer group |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/ConsumerGroupDescribeResponse`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
