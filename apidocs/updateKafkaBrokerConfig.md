# Update broker config

## Overview

- **Method:** `PUT`
- **Path:** `/admin/v1/data/kafka/organizations/{orgName}/clusters/{clusterName}/brokers/{brokerId}/configs`
- **Operation ID:** `updateKafkaBrokerConfig`
- **Tags:** kafka, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | The name of organization |
| `clusterName` | path | true | `string` | The name of cluster |
| `brokerId` | path | true | `integer` | The id of broker |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/UpdateBrokerConfigRequest`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK |  |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
