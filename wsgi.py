"""
WSGI entry point for Vercel
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from api import app

# WSGI application
application = app

# For Vercel
if __name__ == '__main__':
    app.run()
