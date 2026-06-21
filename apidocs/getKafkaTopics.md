# Get all topics in cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/topics`
- **Operation ID:** `getKafkaTopics`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `nameFilter` | query | false | `string` | search pattern, support prefix search |
| `onlyNames` | query | false | `boolean` | if true, only return topic names |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/TopicsList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
