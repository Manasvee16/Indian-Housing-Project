#!/usr/bin/env python
"""
Simple Flask app launcher with error handling
"""
import sys
import os

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from app import app
    print("=" * 60)
    print("Flask App Starting...")
    print("=" * 60)
    print("Local URL: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
