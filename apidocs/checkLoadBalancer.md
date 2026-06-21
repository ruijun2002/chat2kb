# Check if the load balancer is available

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/environments/{environmentName}/loadbalancer/check`
- **Operation ID:** `checkLoadBalancer`
- **Tags:** loadBalancer

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
| `200` | OK |  |
| `403` |  |  |
| `404` |  |  |
