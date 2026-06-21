# List messages from topic

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topic/{topic}/messages`
- **Operation ID:** `listKafkaTopicMessages`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `topic` | path | true | `string` |  |
| `partition` | query | true | `integer` |  |
| `offset` | query | true | `integer` |  |
| `count` | query | false | `integer` | 获取消息的数量 |
| `keyFilter` | query | false | `string` | 消息 key 的过滤条件（大小写不敏感） |
| `valueFilter` | query | false | `string` | 消息内容的过滤条件（大小写不敏感） |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/TopicMessageList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
