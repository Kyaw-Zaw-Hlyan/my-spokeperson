from fastapi import FastAPI
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the FastAPI app from main folder
try:
    # Handle both local and Vercel deployment
    from main_folder.app import app
except ImportError:
    # Fallback for when main_folder doesn't resolve correctly
    import importlib.util
    spec = importlib.util.spec_from_file_location("app", os.path.join(os.path.dirname(os.path.dirname(__file__)), "main folder", "app.py"))
    app_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app_module)
    app = app_module.app

# Export app for Vercel
