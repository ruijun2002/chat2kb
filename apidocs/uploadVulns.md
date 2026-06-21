# Upload vulnerabilities

## Overview

- **Method:** `PUT`
- **Path:** `/admin/v1/vulns`
- **Operation ID:** `uploadVulns`
- **Tags:** vuln

## Description

_No description provided._

## Parameters

_No parameters._

## Request Body

**Content-Type:** `multipart/form-data`
**Ref:** `#/components/schemas/vulnUploadFormData`

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when vulnerabilities are uploaded successfully. |  |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
