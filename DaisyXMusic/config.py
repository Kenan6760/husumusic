from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDA8Pyn5cY0e8qXCHh4QFurZsPsJ-ubmCHmDhSoqeqZTpgR7mlf8XjNh5wWRsDJURZTc3yTYHOMabl0kQYwRDRMiUPMFiPHlMqeZkb0tPHGCAlWsR9A5XvT_5J6PN4NWmVYzxMNuHwtARTYmNpLQ0oKLn-0XfbEW8tF5FQ3HX5-l-Z6lnlS_2FhUmUE71an6JFebOajNx2qvRMauZplzOaKxb3Kp1Lr-TYVWOVY5p8of-vsmL6hK3IY_U9JAFnB97jgQuxIofspOzqPHZ3_pDDioqUChIez-Q12oxnriXOqwBpe1-KtpAiQllCtY2q5GAT6Y88Qo7V82nPEJR9thn9gSib28QA")
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
