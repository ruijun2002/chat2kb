# Delete environment VIP Pool

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/environments/{environmentName}/loadbalancer/vipPool/{poolID}`
- **Operation ID:** `deleteVIPPool`
- **Tags:** vipPool

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `poolID` | path | true | `string` | id of the VIP Pool |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when project is deleted successfully. |  |
| `403` |  |  |
| `404` |  |  |
