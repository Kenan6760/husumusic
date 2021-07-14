from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC3ePuU5ER-aWY04wqQMFyR-S4PODgzf02XmNg3mIkmtMjpIzpZxvGxUuEi11KJpeooG2EkDTSA-dcvYlaZPbJLJn3VBj1OhINHEq96GXiwLKQCNwrW8-5dcToAbrRs1i3E2wVQoDkPJ50vJPNhVhdbyrlqNxWZNBKJCirRMoINiutQNg8fw7tMs8n9YXKVhIYXAEIAm73u4_ieAJhcfOO9o3XRyJIDPEc5jw3WHnGYrZJGTG0rFgYD0OfbXQf30bTDLAO80i_YDWtS8vjpbg19qi80g-SSSUi-rqB9n4rpCJTfXPpTCEXdku9OlrKQ_jrF5BXD4ol3t4iZ9u-6KQsfSib28QA")
BOT_TOKEN = getenv("BOT_TOKEN", "1788475673:AAGf0y7FNNJidnxqgKou5yf8oIoSggap-pc")
BOT_NAME = getenv("BOT_NAME" "Brend")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BrendBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/7072a070ab0ac1bf63ff3.png")
admins = {}
API_ID = int(getenv("API_ID", 1425632))
API_HASH = getenv("API_HASH", "e5861d507c3c2a73a354a3c12f8141f8")
BOT_USERNAME = getenv("BOT_USERNAME", "BrendMusicRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BrendAsistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BrendSup")
PROJECT_NAME = getenv("PROJECT_NAME", "Brend Music")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/Mr_HD_20")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "AIAVSA-ITMFPB-HSZWYO-UURBKY-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1081850094").split()))
