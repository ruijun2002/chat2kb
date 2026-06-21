# get auto inspection

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/autoInspection`
- **Operation ID:** `getAutoInspection`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `id` | query | false | `string` | id of the auto inspection |
| `orgName` | query | false | `string` | name of the Org |
| `envName` | query | false | `string` | name of the environment |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/autoInspection`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
