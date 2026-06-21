# List task types

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/taskTypes`
- **Operation ID:** `listTaskTypes`
- **Tags:** task, shared

## Description

List task types

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Current task type list | `application/json`: **Ref:** `#/components/schemas/taskTypeList`   |
| `400` |  |  |
| `401` |  |  |
| `403` |  |  |
| `500` |  |  |
