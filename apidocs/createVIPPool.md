# Create environment VIP Pool

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/loadbalancer/vipPool`
- **Operation ID:** `createVIPPool`
- **Tags:** vipPool

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |

## Request Body

**Content-Type:** `application/json`
**Ref:** `#/components/schemas/vipPoolCreate`

_Required: true_

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `201` | Returned when environment is created successfully. | `application/json`: **Ref:** `#/components/schemas/vipPool`   |
| `403` |  |  |
| `404` |  |  |
