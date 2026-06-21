# List RabbitMQ accounts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `listRabbitAccounts`
- **Tags:** RabbitMQ, account, shared

## Description

List all RabbitMQ accounts

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
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/RbmqAccountsList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
