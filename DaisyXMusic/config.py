from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBRHEcvadUNrSPx8U-ss9bZR4XG2VyRqw7apNa99N-uwqyhwUl4UsiygdMbLQeYnOVT8hXEu09AFZYyAA-rKySQbSjl43GUllRt3S9gXJ8NzBrSp0UhjtAXIRR_RECde9ad4Fsu4X51g65Su4KcpOseNhzg3XUcS9iVOOXShoYydUZKDtIRgl-4KUXrqBrX38mfUu0-ymcyqwOt4JQpBT0lo6od6Ep5KgHt05LHtlbw7xcW-j3Bxc9L-Z1xKhckvP0ckGO6Y5nxQfcnlE0wh71X3lLKmbHlVR4LLBN8GUdSe5Tm_Ueo-opD6hx4tyr16LNzAtYnQu9vo_ltCVHs_jSCXEmt_AA")
BOT_TOKEN = getenv("BOT_TOKEN", "1788475673:AAGf0y7FNNJidnxqgKou5yf8oIoSggap-pc")
BOT_NAME = getenv("BOT_NAME" "Brend")
MONGODB_URI = os.environ.get("MONGODB_URI" "mongodb+srv://huseyn2003:huseyn2003@cluster0.7ky2a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
BOT_OWNER = int(os.environ.get("BOT_OWNER", "1081850094"))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BrendBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/7072a070ab0ac1bf63ff3.png")
admins = {}
API_ID = int(getenv("API_ID", 1425632))
API_HASH = getenv("API_HASH", "e5861d507c3c2a73a354a3c12f8141f8")
BOT_USERNAME = getenv("BOT_USERNAME", "BrendMusicRobot")
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1081850094))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BrendAsistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BrendSup")
PROJECT_NAME = getenv("PROJECT_NAME", "Brend Music")
SOURCE_CODE = getenv("SOURCE_CODE", "t.me/Mr_HD_20")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "AIAVSA-ITMFPB-HSZWYO-UURBKY-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
LOG_GRP = getenv("LOG_GRP", "-1001456954154")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1081850094 1561868122").split()))
