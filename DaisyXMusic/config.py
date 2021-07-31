from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBnWwr3OBBotQmDL-MCCW-rLbocQmHga6K0BxV_DcyNBOkxOcTPvZA2ElJnTGkES8k5xaYvETelm2KES85KghacK9azC6NSR-FRFcMBrH00zY757OoZxiqZ26NM9z9vxYEUjNslfeI2gpAaF-4Moa0UaQKUpknjsXaVU2oNVBDKmv9Y0SPr60sSlLFX8YIIRob5CKzldyDX5r7AFD6zgosjSnRIx8eoAgcTgWjpO1JbXu8I3gMTh8YByPCjnLXV2tKnQYcLdjniQfmPtTFKK0S6d6sw41xfFCtXapvknQGnBpBfAXWnetgGUNuOIZaNgkcAM6ok8i0xe2eSimbb6rDOXEmt_AA")
BOT_TOKEN = getenv("BOT_TOKEN", "1788475673:AAGf0y7FNNJidnxqgKou5yf8oIoSggap-pc")
BOT_NAME = getenv("BOT_NAME" "Brend")
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
