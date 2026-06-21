# Update RabbitMQ account password

## Overview

- **Method:** `PATCH`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `updateRabbitAccountPassword`
- **Tags:** RabbitMQ, account, shared

## Description

Update a RabbitMQ account password

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | path | true | `string` | name of the Account |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/RbmqUser`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
