# close MongoDB mongosh runtime session

## Overview

- **Method:** `DELETE`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/datasource/{id}/mongodb/shell/sessions/{sessionID}`
- **Operation ID:** `mongoCloseShellSession`
- **Tags:** dms

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` |  |
| `clusterName` | path | true | `string` |  |
| `id` | path | true | `string` |  |
| `sessionID` | path | true | `string` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `204` | shell session closed |  |
| `404` |  |  |
| `500` |  |  |
