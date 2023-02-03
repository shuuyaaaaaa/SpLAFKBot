from config import *

def set_var(var, key):
    os.environ[var] = key

def set_env_vars():
    print("Setting environment variables...")
    set_var("API_ID", str(API_ID))
    set_var("API_HASH", API_HASH)
    set_var("BOT_TOKEN", BOT_TOKEN)
    set_var("MONGO_DB_URI", MONGO_DB_URI)
    set_var("SUDO_USERS", str(SUDO_USERS))
    set_var("START_IMAGE", START_IMAGE)
    set_var("WELCOME_IMAGE", WELCOME_IMAGE)
    set_var("SUPPORT_CHAT", SUPPORT_CHAT)
    set_var("CHANNEL", CHANNEL)
    print("Environment variables set successfully !")

set_env_vars()
