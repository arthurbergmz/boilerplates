from __future__ import annotations

import json
import re
from typing import Any

TYPE_MAP = {
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "object": dict,
    "array": list,
}


def _validate_simple_json_schema(payload: dict[str, Any], schema: dict[str, Any]) -> tuple[bool, str | None]:
    expected_type = schema.get("type")
    if expected_type:
        py_type = TYPE_MAP.get(expected_type)
        if py_type is None:
            return False, f"unsupported schema type: {expected_type}"
        if not isinstance(payload, py_type):
            return False, f"payload must be of type {expected_type}"

    required = schema.get("required", [])
    if isinstance(required, list):
        for key in required:
            if key not in payload:
                return False, f"missing required key: {key}"

    properties = schema.get("properties", {})
    if isinstance(properties, dict):
        for key, prop_schema in properties.items():
            if key not in payload:
                continue
            if not isinstance(prop_schema, dict):
                continue
            prop_type = prop_schema.get("type")
            if not prop_type:
                continue
            py_type = TYPE_MAP.get(prop_type)
            if py_type is None:
                return False, f"unsupported property type for {key}: {prop_type}"
            if not isinstance(payload[key], py_type):
                return False, f"property '{key}' must be of type {prop_type}"

    return True, None


def validate_structured_output(
    text: str,
    schema_type: str | None,
    schema: str | None,
) -> tuple[bool, str | None]:
    """Validate text using lightweight regex or JSON-schema-like checks."""
    if schema_type is None:
        return True, None

    if not schema:
        return False, "schema must be provided when schema_type is set"

    if schema_type == "regex":
        if re.fullmatch(schema, text) is None:
            return False, "text does not match regex schema"
        return True, None

    if schema_type == "json":
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            return False, f"invalid JSON payload: {exc}"

        try:
            schema_obj = json.loads(schema)
        except json.JSONDecodeError as exc:
            return False, f"invalid JSON schema: {exc}"

        if not isinstance(payload, dict):
            return False, "JSON payload must be an object"
        if not isinstance(schema_obj, dict):
            return False, "JSON schema must be an object"

        return _validate_simple_json_schema(payload, schema_obj)

    return False, f"unsupported schema_type: {schema_type}"
