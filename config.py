from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

SUDO_USERS = getenv("SUDO_USERS", "").split()

# BELOW VARS ARE NOT COMPULSORY !

START_IMAGE = getenv("START_IMAGE", "")

WELCOME_IMAGE = getenv("WELCOME_IMAGE", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")

CHANNEL = getenv("CHANNEL", "")

# DO NOT CHANGE THIS

for x in SUDO_USERS:
    SUDO_USERS.append(int(x))
    SUDO_USERS.remove(x)
