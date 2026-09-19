# Homebrew tap notes

This project is prepared for a GitHub-hosted Homebrew tap with a formula that installs the CLI from the GitHub release tarball.

Expected tap layout:

- homebrew-tap/Formula/agentic-audit-tools.rb

Example install flow:

```bash
brew tap inputdrive/tap
brew install agentic-audit-tools
```

If you later want to publish a formula, use the GitHub release asset produced from the tagged source archive.
