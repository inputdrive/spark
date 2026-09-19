import json
import sys
from pathlib import Path

from agentic_audit.cli import main
from agentic_audit.receipt import compare_audit_receipts, write_audit_receipt


def test_compare_audit_receipts_reports_additions_and_removals(tmp_path: Path):
    first = [
        {
            "id": "cursor",
            "name": "Cursor",
            "path": str(tmp_path / "cursor"),
            "exists": True,
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "review metadata",
        }
    ]
    second = [
        {
            "id": "cursor",
            "name": "Cursor",
            "path": str(tmp_path / "cursor"),
            "exists": False,
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "review metadata",
        },
        {
            "id": "claude_code",
            "name": "Claude Code",
            "path": str(tmp_path / "claude"),
            "exists": True,
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "do not read bodies",
        },
    ]

    first_receipt = write_audit_receipt(first, export_path=tmp_path / "first.json", allowed_reader="reviewer")
    second_receipt = write_audit_receipt(second, export_path=tmp_path / "second.json", allowed_reader="reviewer")

    diff = compare_audit_receipts(first_receipt, second_receipt)

    assert diff["status"] == "changed"
    assert diff["added"][0]["artifact_name"] == "Claude Code"
    assert diff["removed"] == []
    assert diff["changed"][0]["artifact_name"] == "Cursor"
    assert json.dumps(diff).find("super-secret") == -1


def test_cli_compare_receipts_reports_delta(tmp_path: Path, monkeypatch, capsys):
    old = [
        {
            "id": "cursor",
            "name": "Cursor",
            "path": str(tmp_path / "cursor"),
            "exists": True,
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "review metadata",
        }
    ]
    new = [
        {
            "id": "cursor",
            "name": "Cursor",
            "path": str(tmp_path / "cursor"),
            "exists": False,
            "sensitivity": "medium",
            "owner": "user",
            "collection_rule": "review metadata",
        },
        {
            "id": "claude_code",
            "name": "Claude Code",
            "path": str(tmp_path / "claude"),
            "exists": True,
            "sensitivity": "high",
            "owner": "user",
            "collection_rule": "do not read bodies",
        },
    ]

    old_path = tmp_path / "old.json"
    new_path = tmp_path / "new.json"
    write_audit_receipt(old, export_path=old_path, allowed_reader="reviewer")
    write_audit_receipt(new, export_path=new_path, allowed_reader="reviewer")

    monkeypatch.setattr(sys, "argv", ["agentic-audit-tools", "--compare", str(old_path), str(new_path)])
    main()
    captured = capsys.readouterr()

    assert '"status": "changed"' in captured.out
    assert '"added"' in captured.out
    assert 'Claude Code' in captured.out
