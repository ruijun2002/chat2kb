# Query event detail by Event ID

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/events/{eventID}`
- **Operation ID:** `getEvent`
- **Tags:** event

## Description

Retrieves detailed information about an event based on the provided Event ID.

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `eventID` | path | true | `string` | Unique identifier for the event. |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Successful operation | `application/json`: **Ref:** `#/components/schemas/event`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
