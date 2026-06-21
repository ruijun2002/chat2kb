# List outage record for environments

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/sla/outages`
- **Operation ID:** `ListEnvironmentOutageRecord`
- **Tags:** SLA

## Description

List outage record for environments

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | query | false | `string` | name of the environment, if not specified, return all environments |
| `orgName` | query | false | `string` | name of the organization |
| `clusterID` | query | false | `string` | id of the cluster |
| `activeOnly` | query | false | `boolean` | whether to return only active outage records |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Outage record retrieved successfully | `application/json`: **Ref:** `#/components/schemas/OutageRecordList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
| `500` |  |  |
