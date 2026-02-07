from fastapi import FastAPI
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_folder.app import app

# Export app for Vercel
