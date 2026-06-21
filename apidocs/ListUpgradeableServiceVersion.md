# list upgraded service version of the component

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/upgradeableServiceVersion`
- **Operation ID:** `ListUpgradeableServiceVersion`
- **Tags:** engine, shared

## Description

list upgraded service version of the component

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `clusterName` | path | true | `string` | Name of the cluster |
| `orgName` | path | true | `string` | organization name |
| `component` | query | true | `string` | component type |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | OK | `application/json`: **Ref:** `#/components/schemas/engineServiceVersions`   |
| `401` |  |  |
| `403` |  |  |
