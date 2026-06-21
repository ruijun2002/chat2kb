# Refresh bill

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/bills/refresh`
- **Operation ID:** `refreshBills`
- **Tags:** billing

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | Returned when bill refreshed successfully. | `application/json`: **Ref:** `#/components/schemas/BasicTask`   |
| `403` |  |  |
| `404` |  |  |
