# list inspection scripts

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/inspectionScripts`
- **Operation ID:** `listInspectionScripts`
- **Tags:** inspection

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgNames` | query | false | `string` | name of the Org, multiple orgs separated by ',', if not provided, return all scripts |
| `engines` | query | false | `string` | query by, such as "node"/"mysql", multiple engines separated by ',' |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Type:** `array` **Items:** **Ref:** `#/components/schemas/inspectionScript`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
