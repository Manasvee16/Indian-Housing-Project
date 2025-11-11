#!/bin/bash
# Vercel build script - optimized for serverless function size
set -e

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Installing Python dependencies..."
# Use pre-built wheels only, no source builds
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir --only-binary :all: -r requirements.txt || \
pip install --no-cache-dir -r requirements.txt

echo "Cleaning up unnecessary files..."
# Remove compiled bytecode
find /usr/local/lib -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -type f -name "*.pyc" -delete 2>/dev/null || true

# Remove test directories and docs
find /usr/local/lib -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -type d -name "test" -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -type d -name "docs" -exec rm -rf {} + 2>/dev/null || true

echo "Build completed successfully"
