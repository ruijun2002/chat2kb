# List environment VIP Pools

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/loadbalancer/vipPool`
- **Operation ID:** `listVIPPool`
- **Tags:** vipPool

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/vipPoolList`   |
| `403` |  |  |
| `404` |  |  |
