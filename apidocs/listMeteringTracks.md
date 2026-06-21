# List metering tracks

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/metering/tracks`
- **Operation ID:** `listMeteringTracks`
- **Tags:** metering

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `clusterID` | query | false | `string` | The ID of the cluster |
| `orgName` | query | false | `string` | Name of organization |
| `projectName` | query | false | `string` | name of the project |
| `environmentName` | query | false | `string` | The name of the environment |
| `pageNumber` | query | false | `integer` | the pageNumber of the query |
| `pageSize` | query | false | `integer` | the pageSize of the query |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | List metering tracks | `application/json`: **Ref:** `#/components/schemas/MeteringTrackList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
