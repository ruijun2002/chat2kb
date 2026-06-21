# List bills

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/bills`
- **Operation ID:** `listBills`
- **Tags:** billing

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `billID` | query | false | `string` | The ID of the bill |
| `clusterID` | query | false | `string` | The ID of the cluster |
| `orgName` | query | false | `string` | name of the organization |
| `projectName` | query | false | `string` | name of the project |
| `aggregationTime` | query | true | `#/components/schemas/aggregationTimeType` | The type of aggregation time |
| `aggregationGroup` | query | true | `#/components/schemas/aggregationGroupType` | The type of aggregation group |
| `` |  | false | `` |  |
| `` |  | false | `` |  |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | List bill details | `application/json`: **Ref:** `#/components/schemas/BillList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
