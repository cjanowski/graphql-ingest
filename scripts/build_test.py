#!/usr/bin/env python3
"""
Build & Distribution Test Script for CSV GraphQL CLI

This script demonstrates the improved packaging setup and builds distributions.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description, capture_output=True):
    """Run a command and show the result."""
    print(f"\n🔧 {description}")
    print(f"Command: {cmd}")
    print("═" * 60)

    try:
        if capture_output:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                print("✅ SUCCESS")
                if result.stdout:
                    lines = result.stdout.strip().split("\n")
                    # Show first few and last few lines for long output
                    if len(lines) > 10:
                        for line in lines[:5]:
                            print(f"  {line}")
                        print(f"  ... ({len(lines) - 10} more lines) ...")
                        for line in lines[-5:]:
                            print(f"  {line}")
                    else:
                        for line in lines:
                            print(f"  {line}")
            else:
                print("❌ FAILED")
                if result.stderr:
                    print(f"  Error: {result.stderr.strip()}")
        else:
            print("Running command...")
            result = subprocess.run(cmd, shell=True)
            print(f"Exit code: {result.returncode}")
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT")
    except Exception as e:
        print(f"💥 ERROR: {e}")


def main():
    """Test package building and distribution."""
    print(
        """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     🏗️  PACKAGE BUILD TEST 🏗️                               ║
║                                                                               ║
║  Testing all the awesome packaging improvements in setup.py!                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    )

    # Package metadata tests
    run_command("python3 setup.py --name", "📦 Package Name")
    run_command("python3 setup.py --version", "🏷️  Package Version")
    run_command("python3 setup.py --description", "📝 Package Description")
    run_command("python3 setup.py --author", "👤 Package Author")
    run_command("python3 setup.py --license", "⚖️  Package License")

    # Validation tests
    run_command("python3 setup.py check --metadata", "✅ Metadata Validation")
    run_command("python3 setup.py check --strict", "🔍 Strict Validation")

    # Build tests
    print(f"\n{'='*60}")
    print("🏗️  BUILDING DISTRIBUTIONS")
    print("=" * 60)

    # Clean up first
    run_command("rm -rf build/ dist/ *.egg-info/", "🧹 Cleaning build artifacts")

    # Build source distribution
    run_command("python3 setup.py sdist", "📦 Building source distribution")

    # Build wheel distribution
    run_command("python3 setup.py bdist_wheel", "🎯 Building wheel distribution")

    # List what was built
    run_command("ls -la dist/", "📋 Listing built distributions")

    # Show package contents
    if Path("dist").exists():
        print(f"\n🎉 SUCCESS! Package distributions built:")
        for dist_file in Path("dist").glob("*"):
            size = dist_file.stat().st_size
            print(f"  📁 {dist_file.name} ({size:,} bytes)")

    print(
        f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         🎊 SETUP.PY IMPROVEMENTS 🎊                          ║
║                                                                               ║
║  ✨ Modern packaging with pyproject.toml support                             ║
║  🔧 Multiple CLI entry points (7 different commands!)                        ║
║  📦 Professional package metadata with URLs and classifiers                  ║
║  🛠️  Development dependencies and extras (dev, test, lint, docs)             ║
║  📋 Proper MANIFEST.in for file inclusion                                    ║
║  🏷️  MIT License and author information                                      ║
║  🎯 Python version requirements (3.8+)                                       ║
║  🔍 Setup validation and error checking                                      ║
║  📝 Beautiful emoji-enhanced descriptions                                    ║
║  🌐 GitHub project URLs for documentation and issues                         ║
║                                                                               ║
║  CLI Commands Available After Installation:                                  ║
║  • csv-graphql  (main CLI)     • csvgql        (short alias)                ║
║  • csv-ingest   (direct)       • csv-serve     (direct)                     ║
║  • csv-preview  (direct)       • csv-tables    (direct)                     ║
║  • csvgql-dev   (dev server)                                                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    )


if __name__ == "__main__":
    main()
