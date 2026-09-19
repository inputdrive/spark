from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _redact_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _redact_value(val) for key, val in value.items()}
    if isinstance(value, list):
        return [_redact_value(item) for item in value]
    if isinstance(value, str):
        lowered = value.lower()
        if any(token in lowered for token in ("key", "token", "secret", "password", "authorization", "bearer")):
            return "[REDACTED]"
        return value
    return value


def parse_mcp_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    data = json.loads(config_path.read_text(encoding="utf-8"))

    servers: dict[str, Any] = {}
    raw_servers = data.get("mcpServers", {}) if isinstance(data, dict) else {}

    for name, details in raw_servers.items():
        if isinstance(details, dict):
            sanitized = {
                "command": details.get("command"),
                "args": details.get("args", []),
                "env": _redact_value(details.get("env", {})),
                "cwd": details.get("cwd"),
            }
            servers[str(name)] = sanitized

    return {
        "kind": "mcp-config",
        "path": str(config_path),
        "server_count": len(servers),
        "servers": servers,
    }


def parse_transcript_metadata(path: str | Path) -> dict[str, Any]:
    transcript_path = Path(path)
    data = json.loads(transcript_path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        return {"kind": "transcript", "path": str(transcript_path), "message_count": 0, "messages": []}

    messages = data.get("messages", []) if isinstance(data, dict) else []
    safe_messages: list[dict[str, Any]] = []
    for message in messages:
        if isinstance(message, dict):
            safe = {
                "role": message.get("role"),
                "content_length": len(str(message.get("content", ""))),
            }
            safe_messages.append(safe)

    redacted = {
        "kind": "transcript",
        "path": str(transcript_path),
        "conversation_id": data.get("conversationId"),
        "message_count": len(safe_messages),
        "messages": safe_messages,
        "token": "[REDACTED]" if data.get("token") else None,
        "title": data.get("title"),
    }
    return redacted
