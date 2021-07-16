import logging
from DaisyXMusic.modules.msg import Messages as tr
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import Message
from DaisyXMusic.access_db import db
from DaisyXMusic.add_user import AddUserToDatabase
from DaisyXMusic.helpers.broadcast import broadcast_handler
from pyrogram.errors import UserNotParticipant
from DaisyXMusic import config
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
from DaisyXMusic.config import BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    await AddUserToDatabase(client, message)
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Qrupunuza əlavə edin 🙋🏻‍♂️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "📲 Yeniliklər", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "💬 Dəstək qrupu", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "👨🏻‍💻 Sahibim 👨🏻‍💻", url=f"https://t.me/brendowner")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await AddUserToDatabase(_, message)
    await message.reply_text(
        f"""**🔴 Brend Music aktivdir ✅**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Dəstək Qrupu", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    await AddUserToDatabase(client, message)
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Məni Qrupunuza əlavə edin 🙋🏻‍♂️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Yeniliklər', url=f"https://t.me/{UPDATES_CHANNEL}"),
             InlineKeyboardButton(text = '💬 Dəstək Qrupu', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = '👨🏻‍💻 Sahibim 👨🏻‍💻', url=f"https://t.me/BrendOwner")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Salam! Telegram qrupları və kanallarının səsli söhbətlərində musiqi səsləndirə bilərəm.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡Kömək üçün buraya vurun🟡", url=f"https://t.me/{SUPPORT_GROUP}?start"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.command("yayim") & filters.reply & filters.user(config.BOT_OWNER) & ~filters.edited)
async def _broadcast(_, m: Message):
    await broadcast_handler(m)


@Client.on_message(filters.private & filters.command("status") & filters.user(config.BOT_OWNER))
async def _status(_, m: Message):
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**DB-də ümumi istifadəçilər: {total_users}**",
        parse_mode="Markdown",
        quote=True
    )
