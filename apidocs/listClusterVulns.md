# List vulnerabilities which affected the cluster

## Overview

- **Method:** `GET`
- **Path:** `/admin/v1/organizations/{orgName}/clusters/{clusterName}/vulns`
- **Operation ID:** `listClusterVulns`
- **Tags:** vuln

## Description

_No description provided._

## Parameters

| Name | In | Required | Type | Description |
|------|----|----------|------|-------------|
| `orgName` | path | true | `string` | name of the Org |
| `clusterName` | path | true | `string` | name of the cluster |

## Request Body

_No request body._

## Responses

| Status | Description | Schema |
|--------|-------------|--------|
| `200` | Returned when vulnerabilities which affected the cluster are listed successfully. | `application/json`: **Ref:** `#/components/schemas/clusterVulns`   |
| `401` |  |  |
| `403` |  |  |
| `404` |  |  |
