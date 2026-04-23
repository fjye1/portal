import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))  # loads .env into os.environ


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY") # or "dev-secret-key"   fallback for dev
    CSFR_KEY = os.environ.get("CSFR")
    EVENT_BUILDER_URL = os.getenv("EVENT_BUILDER_URL")



    SQLALCHEMY_TRACK_MODIFICATIONS = False