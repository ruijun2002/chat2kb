# Get environment status history

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/environments/{environmentName}/statusHistory`
- **Operation ID:** `getEnvironmentStatusHistory`
- **Tags:** environment

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `environmentName` | path | true | `string` | name of the environment |
| `startTime` | query | true | `string` | start time of the query range (nano seconds) |
| `endTime` | query | true | `string` | end time of the query range(nano seconds) |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/environmentStatusHistory`   |
