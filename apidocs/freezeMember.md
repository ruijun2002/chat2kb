# freeze the member in org

## Overview

- **Method:** `POST`
- **Path:** `/admin/v1/organizations/{orgName}/members/{memberId}/freeze`
- **Operation ID:** `freezeMember`
- **Tags:** organization, shared

## Description

freeze the member in org

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `memberId` | path | true | `string` | ID of the member |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | OK |  |
| `401` |  |  |
| `403` |  |  |
