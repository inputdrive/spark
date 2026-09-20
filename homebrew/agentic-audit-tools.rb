class AgenticAuditTools < Formula
  desc "Read-only local audit inventory for agentic coding tools"
  homepage "https://github.com/inputdrive/spark"
  url "https://github.com/inputdrive/spark/archive/refs/tags/v0.2.0.tar.gz"
  sha256 "a62aa5ebcef4b375854f2a6119a85f5917120d8b2113217bdaf762b7847af979"
  license "Apache-2.0"

  depends_on "python@3.12"

  def install
    python_bin = (Formula["python@3.12"].opt_bin/"python3").to_s
    system python_bin, "-m", "pip", "install", "--no-deps", "--prefix=#{prefix}", "."
    bin.install_symlink prefix/"bin/agentic-audit-tools"
  end

  test do
    system "#{bin}/agentic-audit-tools", "--help"
  end
end
