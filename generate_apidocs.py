#!/usr/bin/env python3
"""Generate one Markdown file per API operation from adminapi.yaml."""

import json
import os
import re
import yaml
from pathlib import Path

YAML_FILE = Path(__file__).parent / "adminapi.yaml"
OUT_DIR = Path(__file__).parent / "apidocs"

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}


def sanitize_filename(name: str) -> str:
    """Make a safe filesystem filename."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name) or "api"


def fmt_list(items):
    return ", ".join(str(x) for x in items) if items else "-"


def fmt_value(value):
    """Convert a value to a Markdown-friendly string."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, dict)):
        import json
        return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```"
    return str(value)


def schema_summary(schema: dict) -> str:
    """Return a compact representation of a schema object."""
    if not isinstance(schema, dict):
        return fmt_value(schema)
    parts = []
    if "$ref" in schema:
        parts.append(f"**Ref:** `{schema['$ref']}`")
    if "type" in schema:
        parts.append(f"**Type:** `{schema['type']}`")
    if "description" in schema:
        parts.append(str(schema["description"]))
    if "enum" in schema:
        parts.append(f"**Enum:** {fmt_list(schema['enum'])}")
    if "items" in schema:
        parts.append(f"**Items:** {schema_summary(schema['items'])}")
    if "properties" in schema:
        props = list(schema["properties"].keys())
        parts.append(f"**Properties:** {', '.join(props[:20])}{'...' if len(props) > 20 else ''}")
    return " ".join(parts) if parts else fmt_value(schema)


def render_parameters(params: list) -> str:
    if not params:
        return "_No parameters._\n"
    lines = ["| Name | In | Required | Type | Description |", "|------|----|----------|------|-------------|"]
    for p in params:
        name = p.get("name", "")
        in_ = p.get("in", "")
        required = "true" if p.get("required") else "false"
        schema = p.get("schema", {})
        ptype = schema.get("type", schema.get("$ref", ""))
        desc = p.get("description", "")
        lines.append(f"| `{name}` | {in_} | {required} | `{ptype}` | {desc} |")
    return "\n".join(lines) + "\n"


def render_request_body(body: dict) -> str:
    if not body:
        return "_No request body._\n"
    lines = []
    content = body.get("content", {})
    for content_type, detail in content.items():
        lines.append(f"**Content-Type:** `{content_type}`")
        schema = detail.get("schema", {})
        lines.append(schema_summary(schema))
    required = body.get("required", False)
    if required:
        lines.append("\n_Required: true_")
    return "\n".join(lines) + "\n"


def render_responses(responses: dict) -> str:
    if not responses:
        return "_No responses documented._\n"
    lines = ["| Status | Description | Schema |", "|--------|-------------|--------|"]
    for status, detail in responses.items():
        desc = detail.get("description", "") if isinstance(detail, dict) else ""
        schema = ""
        if isinstance(detail, dict):
            content = detail.get("content", {})
            for ct, cd in content.items():
                schema += f"`{ct}`: {schema_summary(cd.get('schema', {}))}  "
        lines.append(f"| `{status}` | {desc} | {schema} |")
    return "\n".join(lines) + "\n"


def generate():
    if not YAML_FILE.exists():
        raise FileNotFoundError(f"{YAML_FILE} not found")

    with open(YAML_FILE, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    OUT_DIR.mkdir(exist_ok=True)

    index = []
    catalog = []
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, op in methods.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue

            operation_id = op.get("operationId", "")
            summary = op.get("summary", "")
            description = op.get("description", "").strip()
            tags = op.get("tags", [])

            filename = sanitize_filename(operation_id or f"{method}_{path}") + ".md"
            filepath = OUT_DIR / filename

            md = []
            md.append(f"# {summary or operation_id or 'API'}")
            md.append("")
            md.append("## Overview")
            md.append("")
            md.append(f"- **Method:** `{method.upper()}`")
            md.append(f"- **Path:** `{path}`")
            md.append(f"- **Operation ID:** `{operation_id}`")
            md.append(f"- **Tags:** {fmt_list(tags)}")
            md.append("")
            md.append("## Description")
            md.append("")
            md.append(description or "_No description provided._")
            md.append("")
            md.append("## Parameters")
            md.append("")
            md.append(render_parameters(op.get("parameters", [])))
            md.append("## Request Body")
            md.append("")
            md.append(render_request_body(op.get("requestBody")))
            md.append("## Responses")
            md.append("")
            md.append(render_responses(op.get("responses", {})))

            filepath.write_text("\n".join(md), encoding="utf-8")
            index.append((tags[0] if tags else "untagged", summary or operation_id, filename))
            catalog.append({
                "operationId": operation_id,
                "method": method.upper(),
                "path": path,
                "summary": summary,
                "tags": tags,
                "hasPathParams": "{" in path,
                "parameters": [
                    {"name": p.get("name"), "in": p.get("in"), "required": p.get("required", False)}
                    for p in op.get("parameters", [])
                ],
            })

    # Write compact JSON catalog for runtime LLM planning
    catalog_path = Path(__file__).parent / "api_catalog.json"
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")

    # Optional index
    index_path = OUT_DIR / "README.md"
    index.sort(key=lambda x: (x[0].lower(), x[1].lower()))
    lines = ["# Admin API Documentation", "", "| Tag | API | File |", "|-----|-----|------|"]
    current_tag = None
    for tag, name, filename in index:
        lines.append(f"| {tag} | {name} | [{filename}]({filename}) |")
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated {len(index)} API docs in {OUT_DIR}")


if __name__ == "__main__":
    generate()
