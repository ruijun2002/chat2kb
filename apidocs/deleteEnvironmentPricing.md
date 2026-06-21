# Delete the environment pricing

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/pricing`
- **Operation ID:** `deleteEnvironmentPricing`
- **Tags:** pricing

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | true | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when pricing deleted successfully. | `application/json`: **Type:** `object`   |
| `403` |  |  |
| `404` |  |  |
