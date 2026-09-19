import json
from pathlib import Path

from agentic_audit.discover import discover_artifacts
from agentic_audit.receipt import build_audit_receipt, write_audit_receipt


def test_build_audit_receipt_adds_safe_review_fields(tmp_path: Path):
    claude_dir = tmp_path / "Library" / "Application Support" / "Claude"
    claude_dir.mkdir(parents=True)
    config_path = claude_dir / "mcp.json"
    config_path.write_text(
        json.dumps({"mcpServers": {"demo": {"env": {"API_KEY": "super-secret-value"}}}}),
        encoding="utf-8",
    )

    scan_results = discover_artifacts(home_dir=tmp_path, os_name="darwin")
    receipt = build_audit_receipt(
        scan_results,
        os_name="darwin",
        home_dir=str(tmp_path),
        allowed_reader="security-reviewer",
    )

    claude_receipt = next(item for item in receipt["findings"] if item["artifact_name"] == "Claude Code")

    assert receipt["receipt_version"] == "1.0"
    assert receipt["scan_scope"]["os"] == "darwin"
    assert claude_receipt["finding_id"] == "finding-004"
    assert claude_receipt["artifact_path"] == str(claude_dir)
    assert claude_receipt["allowed_reader"] == "security-reviewer"
    assert claude_receipt["redaction_rule"] == "redact_key_names_and_tokens"
    assert "super-secret-value" not in json.dumps(receipt)


def test_write_audit_receipt_exports_json_file(tmp_path: Path):
    scan_results = [
        {
            "id": "github_copilot",
            "name": "GitHub Copilot",
            "path": str(tmp_path / "workspace"),
            "exists": True,
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "Review only metadata.",
        }
    ]
    export_path = tmp_path / "receipts" / "scan.json"

    receipt = write_audit_receipt(scan_results, export_path=export_path, allowed_reader="reviewer")

    assert export_path.exists()
    assert json.loads(export_path.read_text(encoding="utf-8"))["receipt_version"] == "1.0"
    assert receipt["findings"][0]["allowed_reader"] == "reviewer"
