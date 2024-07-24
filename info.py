# ©️biisal jai shree krishna 😎
from os import environ

API_ID = environ.get("API_ID", "25529076")
API_HASH = environ.get("API_HASH", "b8109a26ed1ba595aa5d70d0e38c3806")
BOT_TOKEN = environ.get("BOT_TOKEN", "7299774021:AAHLOAhHR09fvDR9YLMxJTet41DaCA5gw1o")
BOT_NAME = environ.get("BOT_NAME", "PRIVT GPT")
ADMIN = int(environ.get("ADMIN", ""))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1001796577232"))
ADMIN_NAME = environ.get("ADMIN_NAME", "Bisal")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "")
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://avinashkakde646:avinashkakde646@cluster0.jlubkn6.mongodb.net/?retryWrites=true&w=majority")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-100XXXXXXXXXX")
)  # add your channel id for force subscribe
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
