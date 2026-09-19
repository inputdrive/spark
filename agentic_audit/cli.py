from __future__ import annotations

import argparse
import json

from .discover import discover_artifacts
from .receipt import compare_audit_receipts, load_audit_receipt, write_audit_receipt, write_audit_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Report local agentic tool artifact locations without reading file contents.")
    parser.add_argument("--os", dest="os_name", help="Operating system name, such as darwin, linux, or windows.")
    parser.add_argument("--home-dir", dest="home_dir", help="Home directory to inspect. Defaults to the current user home.")
    parser.add_argument("--receipt-path", dest="receipt_path", help="Optional path for a local audit receipt JSON export.")
    parser.add_argument("--summary-path", dest="summary_path", help="Optional path for a local human-readable audit receipt summary export.")
    parser.add_argument("--allowed-reader", dest="allowed_reader", default="security-reviewer", help="Role or recipient permitted to review the receipt.")
    parser.add_argument("--compare", nargs=2, metavar=("OLD_RECEIPT", "NEW_RECEIPT"), help="Compare two saved receipt JSON files and print the metadata-only diff.")
    args = parser.parse_args()

    if args.compare:
        old_receipt = load_audit_receipt(args.compare[0])
        new_receipt = load_audit_receipt(args.compare[1])
        diff = compare_audit_receipts(old_receipt, new_receipt)
        print(json.dumps(diff, indent=2, sort_keys=True))
        return

    payload = discover_artifacts(home_dir=args.home_dir, os_name=args.os_name)
    if args.receipt_path:
        receipt = write_audit_receipt(
            payload,
            export_path=args.receipt_path,
            os_name=args.os_name,
            home_dir=args.home_dir,
            allowed_reader=args.allowed_reader,
        )
        if args.summary_path:
            summary_text = write_audit_summary(receipt, export_path=args.summary_path)
            print(summary_text)
        else:
            print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
