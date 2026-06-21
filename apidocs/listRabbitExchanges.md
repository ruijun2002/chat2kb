# List RabbitMQ exchanges

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/exchanges`
- **Operation ID:** `listRabbitExchanges`
- **Tags:** RabbitMQ, exchange, shared

## Description

List RabbitMQ exchanges

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/RbmqExchangeList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
