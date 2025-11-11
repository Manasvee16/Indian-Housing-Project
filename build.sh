#!/bin/bash
# Vercel build script
set -e

echo "Python version:"
python --version

echo "Pip version:"
pip --version

echo "Installing Python dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Build completed successfully"
