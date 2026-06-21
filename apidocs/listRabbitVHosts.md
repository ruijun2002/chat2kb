# List RabbitMQ vhosts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/vhosts`
- **Operation ID:** `listRabbitVHosts`
- **Tags:** RabbitMQ, vhost, shared

## Description

List RabbitMQ vhosts

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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/RbmqVHostList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
