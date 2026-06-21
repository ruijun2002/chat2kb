# Create RabbitMQ account

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts`
- **Operation ID:** `createRabbitAccount`
- **Tags:** RabbitMQ, account, shared

## Description

Create a new RabbitMQ account

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/RbmqAccountRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
