from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BrendBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/7072a070ab0ac1bf63ff3.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BrendAsistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BrendSup")
PROJECT_NAME = getenv("PROJECT_NAME", "Brend Music")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/Mr_HD_20")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = getenv("SUDO_USERS")
