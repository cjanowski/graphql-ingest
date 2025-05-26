#!/usr/bin/env python3
"""
Simple wrapper script for the CSV GraphQL CLI
Makes it easier to run without the module syntax.
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Run the CLI with all passed arguments."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    # Run the CLI module with all arguments
    cmd = [sys.executable, "-m", "src.cli"] + sys.argv[1:]

    try:
        # Execute in the script directory
        result = subprocess.run(cmd, cwd=script_dir)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully - just exit cleanly
        sys.exit(130)  # Standard exit code for Ctrl+C (128 + 2)


if __name__ == "__main__":
    main()
