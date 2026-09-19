from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _hash_value(value: str | None) -> str | None:
    if value is None:
        return None
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def build_audit_receipt(
    findings: list[dict[str, Any]],
    *,
    os_name: str | None = None,
    home_dir: str | None = None,
    allowed_reader: str | None = None,
    export_path: str | Path | None = None,
) -> dict[str, Any]:
    normalized_findings: list[dict[str, Any]] = []
    for idx, finding in enumerate(findings, start=1):
        normalized_findings.append(
            {
                "finding_id": f"finding-{idx:03d}",
                "artifact_path": finding.get("path"),
                "artifact_name": finding.get("name"),
                "exists": bool(finding.get("exists", False)),
                "sensitivity": finding.get("sensitivity"),
                "owner": finding.get("owner"),
                "collection_rule": finding.get("collection_rule"),
                "redaction_rule": "redact_key_names_and_tokens",
                "mcp_config_hash": None,
                "transcript_source": None,
                "allowed_reader": allowed_reader,
                "export_path": str(export_path) if export_path is not None else None,
            }
        )

    receipt = {
        "receipt_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scan_scope": {
            "os": os_name or "unknown",
            "home_dir": home_dir,
        },
        "findings": normalized_findings,
    }
    return receipt


def write_audit_receipt(
    findings: list[dict[str, Any]],
    *,
    export_path: str | Path,
    os_name: str | None = None,
    home_dir: str | None = None,
    allowed_reader: str | None = None,
) -> dict[str, Any]:
    path = Path(export_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    receipt = build_audit_receipt(
        findings,
        os_name=os_name,
        home_dir=home_dir,
        allowed_reader=allowed_reader,
        export_path=path,
    )
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    return receipt
