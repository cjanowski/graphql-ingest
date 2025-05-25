#!/bin/bash

# Script to upload to Production PyPI
# Usage: 
#   export TWINE_PASSWORD=your-pypi-token
#   ./upload_to_pypi.sh

echo "🚀 Uploading to Production PyPI..."

# Set username to __token__ for API token authentication
export TWINE_USERNAME=__token__

# Check if TWINE_PASSWORD is set
if [ -z "$TWINE_PASSWORD" ]; then
    echo "❌ Error: TWINE_PASSWORD environment variable not set"
    echo "Please set it to your PyPI API token:"
    echo "export TWINE_PASSWORD=your-pypi-token-here"
    exit 1
fi

# Confirm before uploading to production
read -p "Are you sure you want to upload to PRODUCTION PyPI? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Upload cancelled"
    exit 1
fi

# Upload to PyPI
python -m twine upload dist/*

echo "✅ Upload complete! Check: https://pypi.org/project/csv-graphql-cli/" 