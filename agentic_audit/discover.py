from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from .catalog import catalog_for_os
except ImportError:  # pragma: no cover - supports direct script execution
    from catalog import catalog_for_os


def _qualified_path(home_dir: Path, candidate: str) -> Path:
    candidate_path = Path(candidate).expanduser()
    if candidate_path.is_absolute():
        return candidate_path
    return (home_dir / candidate_path).resolve(strict=False)


def discover_artifacts(home_dir: str | Path | None = None, os_name: str | None = None) -> list[dict[str, Any]]:
    base = Path(home_dir).expanduser() if home_dir is not None else Path.home()
    results: list[dict[str, Any]] = []

    for rule in catalog_for_os(os_name):
        for candidate in rule["paths"]:
            path = _qualified_path(base, candidate)
            exists = path.exists()
            record: dict[str, Any] = {
                "id": rule["id"],
                "name": rule["name"],
                "path": str(path),
                "exists": exists,
                "sensitivity": rule["sensitivity"],
                "owner": rule["owner"],
                "collection_rule": rule["collection_rule"],
            }
            results.append(record)

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Report local agentic tool artifact locations without reading file contents.")
    parser.add_argument("--os", dest="os_name", help="Operating system name, such as darwin, linux, or windows. Defaults to auto-detected platform.")
    parser.add_argument("--home-dir", dest="home_dir", help="Home directory to inspect. Defaults to the current user home.")
    args = parser.parse_args()

    payload = discover_artifacts(home_dir=args.home_dir, os_name=args.os_name)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
