# List cloud providers

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/providers`
- **Operation ID:** `listCloudProviders`
- **Tags:** provider

## Description

List cloud providers

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/providerList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
