import os
from dotenv import load_dotenv

# Load .env file if it exists (local development)
load_dotenv()

# --- Flask ---
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

# --- Database ---
DB_CONFIG = {
    "host":     os.environ.get("DB_HOST",     "localhost"),
    "port":     int(os.environ.get("DB_PORT", "3306")),
    "user":     os.environ.get("DB_USER",     "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME",     "tour_booking"),
    "charset":  "utf8mb4",
}

# --- Environment ---
DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
