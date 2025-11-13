from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = getenv("APP_NAME", "Ayudemos a Fabio")
    DESCRIPTION = getenv("DESCRIPTION", "Una api para ayudar a encontrar una cura para Fabio Martínez")
    VERSION = getenv("VERSION", "0.1.5")

    GOOGLE_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET", "")
    GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID", "")

    WORKSPACE_URL = getenv("WORKSPACE_URL", "")
    WORKSPACE_KEY = getenv("WORKSPACE_KEY", "")
    DONATIONS_URL = getenv("DONATIONS_URL", "")
    DONATIONS_KEY = getenv("DONATIONS_KEY", "")