from os import getenv
import os

API_ID = int(getenv("API_ID", "13691707"))
API_HASH = getenv("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

BOT_TOKEN = getenv("BOT_TOKEN", "5897974176:AAE4eOrMUveQY8BODuMGTLRuwE1WmEkkP5E")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://alpha:<password>@cluster0.zeiqsnj.mongodb.net/?retryWrites=true&w=majority")

SUDO_USERS = getenv("SUDO_USERS", "").split()

# BELOW VARS ARE NOT COMPULSORY !

# LEAVE IT EMPTY, IT WILL TAKE THEM AS DEFAULT

START_IMAGE = getenv("START_IMAGE", "")

WELCOME_IMAGE = getenv("WELCOME_IMAGE", "")

# ENTER CHAT USERNAMES WITHOUT @ ELSE LEAVE THEM EMPTY

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")

CHANNEL = getenv("CHANNEL", "")

# DO NOT CHANGE THIS

for x in SUDO_USERS:
    SUDO_USERS.append(int(x))
    SUDO_USERS.remove(x)
