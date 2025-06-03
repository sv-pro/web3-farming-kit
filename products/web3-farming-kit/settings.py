from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os
class Settings:
    # Telegram bot settings
    TELEGRAM_BOT_USERNAME: str = os.getenv("TELEGRAM_BOT_USERNAME", "")
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "")
    # Database settings
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "retrodrops")
    # Other settings can be added here as needed
settings = Settings()
# Example usage:
# print(settings.TELEGRAM_BOT_USERNAME)
