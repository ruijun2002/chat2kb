# Delete RabbitMQ account

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/data/rabbitmq/organizations/{orgName}/clusters/{clusterName}/accounts/{accountName}`
- **Operation ID:** `deleteRabbitAccount`
- **Tags:** RabbitMQ, account, shared

## Description

Delete a RabbitMQ account

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the Cluster |
| `accountName` | path | true | `string` | name of the Account |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | A successful response. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
