from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REDACTION_RULE_ID = "redact_key_names_and_tokens"


def _hash_value(value: str | None) -> str | None:
    if value is None:
        return None
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def summarize_audit_receipt(receipt: dict[str, Any]) -> dict[str, Any]:
    findings = receipt.get("findings", [])
    return {
        "receipt_version": receipt.get("receipt_version"),
        "generated_at_utc": receipt.get("generated_at_utc"),
        "total_findings": len(findings),
        "redaction_rule_id": DEFAULT_REDACTION_RULE_ID,
        "allowed_readers": sorted({item.get("allowed_reader") for item in findings if item.get("allowed_reader")}),
    }


def compare_audit_receipts(old_receipt: dict[str, Any], new_receipt: dict[str, Any]) -> dict[str, Any]:
    old_by_id = {item["finding_id"]: item for item in old_receipt.get("findings", [])}
    new_by_id = {item["finding_id"]: item for item in new_receipt.get("findings", [])}

    old_ids = set(old_by_id)
    new_ids = set(new_by_id)
    added = [new_by_id[fid] for fid in sorted(new_ids - old_ids)]
    removed = [old_by_id[fid] for fid in sorted(old_ids - new_ids)]
    overlapping = sorted(old_ids & new_ids)
    changed = []

    for finding_id in overlapping:
        old_item = old_by_id[finding_id]
        new_item = new_by_id[finding_id]
        if old_item.get("exists") != new_item.get("exists") or old_item.get("artifact_path") != new_item.get("artifact_path"):
            changed.append({
                "finding_id": finding_id,
                "artifact_name": new_item.get("artifact_name"),
                "before": {
                    "exists": old_item.get("exists"),
                    "artifact_path": old_item.get("artifact_path"),
                },
                "after": {
                    "exists": new_item.get("exists"),
                    "artifact_path": new_item.get("artifact_path"),
                },
            })

    status = "same"
    if added or removed or changed:
        status = "changed"

    return {
        "status": status,
        "added": added,
        "removed": removed,
        "changed": changed,
        "redaction_rule_id": DEFAULT_REDACTION_RULE_ID,
    }


def load_audit_receipt(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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
                "redaction_rule_id": DEFAULT_REDACTION_RULE_ID,
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


def write_audit_summary(receipt: dict[str, Any], *, export_path: str | Path) -> str:
    path = Path(export_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    summary = summarize_audit_receipt(receipt)
    lines = [
        "# Audit Receipt Summary",
        "",
        f"- Receipt version: {summary['receipt_version']}",
        f"- Generated at: {summary['generated_at_utc']}",
        f"- Total findings: {summary['total_findings']}",
        f"- Redaction rule: {summary['redaction_rule_id']}",
        f"- Allowed readers: {', '.join(summary['allowed_readers']) if summary['allowed_readers'] else 'none'}",
        "",
        "## Findings",
    ]

    for finding in receipt.get("findings", []):
        lines.append(
            f"- {finding.get('finding_id')}: {finding.get('artifact_name')} ({finding.get('artifact_path')})"
        )

    content = "\n".join(lines) + "\n"
    path.write_text(content, encoding="utf-8")
    return content
