#!/bin/bash
# Vercel build script - aggressive size optimization for serverless
set -e

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Installing Python dependencies..."
pip install --upgrade pip setuptools wheel

# Install with maximum size optimization
pip install --no-cache-dir --no-binary :all: -r requirements.txt 2>/dev/null || pip install --no-cache-dir -r requirements.txt

echo "Cleaning up unnecessary files to reduce size..."
# Remove compiled bytecode and caches
find /usr/local/lib -name "*.pyc" -delete 2>/dev/null || true
find /usr/local/lib -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -name "*.egg-info" -type d -exec rm -rf {} + 2>/dev/null || true

# Remove tests and documentation
find /usr/local/lib -path "*/tests" -type d -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -path "*/test" -type d -exec rm -rf {} + 2>/dev/null || true
find /usr/local/lib -name "*.so.debug" -delete 2>/dev/null || true
find /usr/local/lib -name "*.a" -delete 2>/dev/null || true

# CatBoost specific cleanup - remove CUDA/GPU support files if present
find /usr/local/lib -path "*/catboost/*" -name "*.cu" -delete 2>/dev/null || true

echo "Build completed successfully"
