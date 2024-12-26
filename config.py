from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27360642"))
API_HASH = getenv("API_HASH", "3159ea7d00a3c266bfbdb45fbf7fe91f")

BOT_TOKEN = getenv("BOT_TOKEN", "8120562276:AAHVyD_2E8J45GdsdlQkg3hCUhfWks1sxoY")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = intgetenv("OWNER_ID", "7078122796")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/beast_fox_network")
