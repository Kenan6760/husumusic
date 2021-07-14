import requests
from pyrogram import Client as Bot

from DaisyXMusic.config import API_HASH
from DaisyXMusic.config import API_ID
from DaisyXMusic.config import BG_IMAGE
from DaisyXMusic.config import BOT_TOKEN
from DaisyXMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DaisyXMusic.modules"),
)

bot.start()
run()
