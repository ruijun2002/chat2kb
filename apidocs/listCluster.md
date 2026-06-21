# List clusters in the Org

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters`
- **Operation ID:** `listCluster`
- **Tags:** cluster, shared

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterDefinition` | query | false | `string` | The clusterDefinition in the List request |
| `environmentName` | query | false | `string` | Environment Type |
| `environmentType` | query | false | `#/components/schemas/environmentType` | Environment Type |
| `tagKey` | query | false | `string` | Tag key; this parameter is deprecated, use tagKeys instead |
| `tagValue` | query | false | `string` | Tag value; this parameter is deprecated, use tagValues instead |
| `tagKeys` | query | false | `array` | A list of tags' keys |
| `tagValues` | query | false | `array` | A list of tags' values corresponding to the tagKeys |
| `licenseId` | query | false | `integer` | license id |
| `refClusterName` | query | false | `string` | list clusters referenced by this cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | A successful response. | `application/json`: **Ref:** `#/components/schemas/clusterList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
