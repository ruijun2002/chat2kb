# List vulnerabilities

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/vulns`
- **Operation ID:** `listVulns`
- **Tags:** vuln

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when vulnerabilities are listed successfully. | `application/json`: **Ref:** `#/components/schemas/vulnList`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
