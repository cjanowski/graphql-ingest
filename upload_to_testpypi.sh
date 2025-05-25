#!/bin/bash

# Script to upload to TestPyPI
# Usage: 
#   export TWINE_PASSWORD=your-testpypi-token
#   ./upload_to_testpypi.sh

echo "🚀 Uploading to TestPyPI..."

# Set username to __token__ for API token authentication
export TWINE_USERNAME=__token__

# Check if TWINE_PASSWORD is set
if [ -z "$TWINE_PASSWORD" ]; then
    echo "❌ Error: TWINE_PASSWORD environment variable not set"
    echo "Please set it to your TestPyPI API token:"
    echo "export TWINE_PASSWORD=your-testpypi-token-here"
    exit 1
fi

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

echo "✅ Upload complete! Check: https://test.pypi.org/project/csv-graphql-cli/" 