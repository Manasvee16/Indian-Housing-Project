#!/bin/bash
# Vercel build script - optimized for serverless function size
set -e

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Installing Python dependencies..."
pip install --upgrade pip setuptools wheel

# Install with size optimization flags
pip install --no-cache-dir -r requirements.txt

# Clean up unnecessary files to reduce size
find /usr -name "*.pyc" -delete 2>/dev/null || true
find /usr -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find /usr -name "tests" -type d -exec rm -rf {} + 2>/dev/null || true

echo "Build completed successfully"
