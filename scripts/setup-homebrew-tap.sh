#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TAP_REPO_DIR="${1:-${HOME}/Code/inputdrive-homebrew-tap}"
TAP_ORG="inputdrive"
TAP_NAME="homebrew-tap"
FORMULA_NAME="agentic-audit-tools"
FORMULA_PATH="${TAP_REPO_DIR}/Formula/${FORMULA_NAME}.rb"

mkdir -p "$(dirname "${TAP_REPO_DIR}")"

if [ ! -d "${TAP_REPO_DIR}/.git" ]; then
  if [ -n "${GITHUB_TOKEN:-}" ]; then
    git clone "https://github.com/${TAP_ORG}/${TAP_NAME}.git" "${TAP_REPO_DIR}"
  else
    mkdir -p "${TAP_REPO_DIR}"
    git -C "${TAP_REPO_DIR}" init
    git -C "${TAP_REPO_DIR}" branch -M main
  fi
fi

mkdir -p "$(dirname "${FORMULA_PATH}")"
cat > "${FORMULA_PATH}" <<'EOF'
class AgenticAuditTools < Formula
  desc "Read-only local audit inventory for agentic coding tools"
  homepage "https://github.com/inputdrive/spark"
  url "https://github.com/inputdrive/spark/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "cf1bcc3aa9733e36b20dd74bd2affba6e3a2e1e271c5bdefe6f77e8d46523caa"
  license "Apache-2.0"

  depends_on "python@3.12"

  def install
    venv = virtualenv_create(libexec, "python3")
    system "#{venv}/bin/python", "-m", "pip", "install", "."
    bin.install_symlink libexec/"bin/agentic-audit-tools"
  end

  test do
    system "#{bin}/agentic-audit-tools", "--help"
  end
end
EOF

git -C "${TAP_REPO_DIR}" add Formula/${FORMULA_NAME}.rb
if ! git -C "${TAP_REPO_DIR}" diff --cached --quiet; then
  git -C "${TAP_REPO_DIR}" commit -m "Add ${FORMULA_NAME} formula"
fi

if ! git -C "${TAP_REPO_DIR}" remote get-url origin >/dev/null 2>&1; then
  git -C "${TAP_REPO_DIR}" remote add origin "https://github.com/${TAP_ORG}/${TAP_NAME}.git"
fi

echo "Tap repo ready at: ${TAP_REPO_DIR}"
echo "Formula path: ${FORMULA_PATH}"
echo "Push with: git -C \"${TAP_REPO_DIR}\" push -u origin main"
echo "Install with: brew tap ${TAP_ORG}/tap && brew install ${FORMULA_NAME}"
