import json
from pathlib import Path

from agentic_audit.parsers import parse_mcp_config, parse_transcript_metadata


def test_parse_mcp_config_redacts_secrets(tmp_path: Path):
    config_path = tmp_path / "mcp.json"
    config_path.write_text(
        json.dumps(
            {
                "mcpServers": {
                    "demo": {
                        "command": "npx",
                        "args": ["server.js"],
                        "env": {"API_KEY": "super-secret-value", "PORT": "3000"},
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    parsed = parse_mcp_config(config_path)

    assert parsed["kind"] == "mcp-config"
    assert parsed["servers"]["demo"]["command"] == "npx"
    assert parsed["servers"]["demo"]["env"]["API_KEY"] == "[REDACTED]"
    assert "super-secret-value" not in json.dumps(parsed)


def test_parse_transcript_metadata_omits_raw_content(tmp_path: Path):
    transcript = tmp_path / "chat.json"
    transcript.write_text(
        json.dumps(
            {
                "conversationId": "abc123",
                "messages": [
                    {"role": "user", "content": "Tell me the secret token = abc123"},
                    {"role": "assistant", "content": "I cannot reveal that."},
                ],
                "token": "real-secret-token",
            }
        ),
        encoding="utf-8",
    )

    parsed = parse_transcript_metadata(transcript)

    assert parsed["kind"] == "transcript"
    assert parsed["message_count"] == 2
    assert parsed["token"] == "[REDACTED]"
    assert "Tell me the secret token" not in json.dumps(parsed)
