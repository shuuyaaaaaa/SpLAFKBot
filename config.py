from os import getenv
import os

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

SUDO_USERS = getenv("SUDO_USERS", "").split()

# BELOW VARS ARE NOT COMPULSORY !

# LEAVE IT EMPTY, IT WILL TAKE THEM AS DEFAULT

START_IMAGE = getenv("START_IMAGE", "")

WELCOME_IMAGE = getenv("WELCOME_IMAGE", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")

CHANNEL = getenv("CHANNEL", "")

# DO NOT CHANGE THIS

for x in SUDO_USERS:
    SUDO_USERS.append(int(x))
    SUDO_USERS.remove(x)
