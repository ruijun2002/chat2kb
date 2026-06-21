# List restore tasks

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/restoreTasks`
- **Operation ID:** `listRestores`
- **Tags:** restore

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | query | false | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/restoreList`   |
| `401` |  |  |
| `403` |  |  |
