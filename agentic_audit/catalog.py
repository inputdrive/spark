from __future__ import annotations

import platform
from typing import Any


def _darwin_rules() -> list[dict[str, Any]]:
    return [
        {
            "id": "cursor",
            "name": "Cursor",
            "paths": [
                "Library/Application Support/Cursor",
                "Library/Application Support/Cursor/User/globalStorage",
                "Library/Application Support/Cursor/User/workspaceStorage",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Review only directory existence and generated metadata; do not read contents.",
            "description": "Cursor editor state, project storage, and recent workspace metadata.",
        },
        {
            "id": "claude_code",
            "name": "Claude Code",
            "paths": [
                "Library/Application Support/Claude",
                "Library/Application Support/Claude/Logs",
            ],
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "Inspect file and directory names without reading file bodies or secrets.",
            "description": "Claude session data, logs, and potentially conversation-related storage.",
        },
        {
            "id": "github_copilot",
            "name": "GitHub Copilot",
            "paths": [
                "Library/Application Support/Code/User/globalStorage/github.copilot-chat",
                "Library/Application Support/Code/User/workspaceStorage",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Report metadata for Copilot workspace storage without reading transcripts or secrets.",
            "description": "Editor-integrated Copilot state such as workspace and chat storage.",
        },
        {
            "id": "mcp_servers",
            "name": "MCP server configuration",
            "paths": [
                ".config",
                ".vscode-server",
                ".cursor/mcp.json",
            ],
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "Read only file names and structure; do not print configuration values or tokens.",
            "description": "MCP and local tool configuration that may include endpoints, credentials, or tool settings.",
        },
    ]


def _linux_rules() -> list[dict[str, Any]]:
    return [
        {
            "id": "cursor",
            "name": "Cursor",
            "paths": [
                ".config/Cursor",
                ".local/share/Cursor",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Review only directory existence and generated metadata; do not read contents.",
            "description": "Cursor editor data and workspace history.",
        },
        {
            "id": "claude_code",
            "name": "Claude Code",
            "paths": [
                ".config/Claude",
                ".local/share/Claude",
            ],
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "Inspect file and directory names without reading file bodies or secrets.",
            "description": "Claude session data and logs.",
        },
        {
            "id": "github_copilot",
            "name": "GitHub Copilot",
            "paths": [
                ".config/github-copilot",
                ".vscode-server/data/User/globalStorage/github.copilot-chat",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Report metadata for Copilot workspace storage without reading transcripts or secrets.",
            "description": "Editor-integrated Copilot state.",
        },
    ]


def _windows_rules() -> list[dict[str, Any]]:
    return [
        {
            "id": "cursor",
            "name": "Cursor",
            "paths": [
                "AppData/Roaming/Cursor",
                "AppData/Roaming/Cursor/User/globalStorage",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Review only directory existence and generated metadata; do not read contents.",
            "description": "Cursor editor state.",
        },
        {
            "id": "claude_code",
            "name": "Claude Code",
            "paths": [
                "AppData/Roaming/Claude",
                "AppData/Local/Claude",
            ],
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "Inspect file and directory names without reading file bodies or secrets.",
            "description": "Claude session data and logs.",
        },
        {
            "id": "github_copilot",
            "name": "GitHub Copilot",
            "paths": [
                "AppData/Roaming/Code/User/globalStorage/github.copilot-chat",
                "AppData/Roaming/Code/User/workspaceStorage",
            ],
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Report metadata for Copilot workspace storage without reading transcripts or secrets.",
            "description": "GitHub Copilot workspace metadata.",
        },
    ]


def detect_os_name() -> str:
    system_name = platform.system().lower()
    if system_name.startswith("darwin") or system_name.startswith("mac"):
        return "darwin"
    if system_name.startswith("linux"):
        return "linux"
    if system_name.startswith("win"):
        return "windows"
    return system_name


def catalog_for_os(os_name: str | None = None) -> list[dict[str, Any]]:
    normalized = (os_name or detect_os_name()).lower()
    if normalized.startswith("darwin"):
        return _darwin_rules()
    if normalized.startswith("linux"):
        return _linux_rules()
    if normalized.startswith("win"):
        return _windows_rules()
    return _darwin_rules() + _linux_rules() + _windows_rules()
