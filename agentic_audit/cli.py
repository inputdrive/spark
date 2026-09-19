from __future__ import annotations

import argparse
import json

from .discover import discover_artifacts


def main() -> None:
    parser = argparse.ArgumentParser(description="Report local agentic tool artifact locations without reading file contents.")
    parser.add_argument("--os", dest="os_name", help="Operating system name, such as darwin, linux, or windows.")
    parser.add_argument("--home-dir", dest="home_dir", help="Home directory to inspect. Defaults to the current user home.")
    args = parser.parse_args()

    payload = discover_artifacts(home_dir=args.home_dir, os_name=args.os_name)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
