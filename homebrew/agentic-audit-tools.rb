class AgenticAuditTools < Formula
  desc "Read-only local audit inventory for agentic coding tools"
  homepage "https://github.com/inputdrive/spark"
  url "https://github.com/inputdrive/spark/archive/refs/tags/v0.2.0.tar.gz"
  sha256 "a6bb29f9a9516f6adb714e9f1851c20ad1448cebbf4552bae4579bb17e383112"
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
