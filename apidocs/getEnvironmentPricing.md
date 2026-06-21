# Get the environment pricing

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/pricing`
- **Operation ID:** `getEnvironmentPricing`
- **Tags:** pricing

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `string` | name of the environment (if provided, returns a list with one item; if omitted, returns all environment prices) |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Retrieve the price of environment(s) as a list | `application/json`: **Ref:** `#/components/schemas/environmentPricingList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
