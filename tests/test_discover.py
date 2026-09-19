import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agentic_audit.catalog import catalog_for_os
from agentic_audit.discover import discover_artifacts


def test_catalog_has_expected_entries():
    catalog = catalog_for_os("darwin")
    ids = {rule["id"] for rule in catalog}

    assert "cursor" in ids
    assert "claude_code" in ids
    assert "github_copilot" in ids
    assert all("paths" in rule for rule in catalog)


def test_discover_reports_only_metadata_without_file_contents(tmp_path):
    claude_dir = tmp_path / "Library" / "Application Support" / "Claude"
    claude_dir.mkdir(parents=True)
    secret_file = claude_dir / "settings.json"
    secret_file.write_text('{"api_key": "super-secret-value"}', encoding="utf-8")

    results = discover_artifacts(home_dir=tmp_path, os_name="darwin")
    claude_match = next(item for item in results if item["id"] == "claude_code")

    assert claude_match["path"] == str(claude_dir)
    assert claude_match["exists"] is True
    assert "super-secret-value" not in json.dumps(results)
