# Changelog

All notable changes to this project will be documented in this file.

## [0.2.1] - 2026-09-22

### Changed
- discovery now auto-detects the current operating system when `--os` is not provided
- CLI receipt generation now records the resolved OS in scan scope without requiring `--os`
- README examples now default to OS auto-detection and document `--os` as an override

### Fixed
- default catalog selection no longer falls back to all platform rules when OS is omitted

## [0.2.0] - 2026-09-19

### Added
- audit receipt generation for scan output
- receipt export option in the CLI
- safe metadata envelope for local review workflows
- receipt-to-receipt comparison for delta review across scans
- markdown receipt summary export for human review

### Changed
- README quick start now includes a local receipt export example
- project roadmap now records the receipt-first milestone
- audit receipt specification is now documented in the repository for future development

### Security
- receipt output remains metadata-only and does not expose secret-bearing values
- redaction rules are tracked explicitly in the receipt payload

## [0.1.0] - 2026-09-19

### Added
- initial local-only discovery catalog for macOS, Linux, and Windows
- metadata-only artifact discovery without reading file contents
- redaction-safe parsing for MCP config files and transcript metadata
- project documentation and public release materials
