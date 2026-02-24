"""Configuration for AI Research Assistant - 100% Free Tools."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings."""
    
    # Google AI Studio API Key (Free, no credit card)
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    
    # Model settings
    MODEL_NAME = "gemini-1.5-flash"
    TEMPERATURE = 0.7
    MAX_TOKENS = 2048
    
    # Database
    DB_PATH = Path("database/knowledge_base.db")
    
    # Search settings
    MAX_SEARCH_RESULTS = 5
    
    # App settings
    APP_TITLE = "🤖 Personal AI Research & Task Assistant"

settings = Settings()

# Validate Google API key
if not settings.GOOGLE_API_KEY:
    print("⚠️  Warning: GOOGLE_API_KEY not found in .env file")
    print("Get your FREE API key at: https://aistudio.google.com/app/apikey")
