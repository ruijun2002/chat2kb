# enable the organization

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/enable`
- **Operation ID:** `enableOrg`
- **Tags:** organization

## Description

enable the organization

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `401` |  |  |
| `403` |  |  |
