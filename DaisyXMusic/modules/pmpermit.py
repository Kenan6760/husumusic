from pyrogram import Client
import asyncio
from DaisyXMusic.config import SUDO_USERS
from DaisyXMusic.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from DaisyXMusic.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam, bu Brend Asistant xidmətidir.\n\n ❗️ Qaydalar:\n   - Söhbətə icazə verilmir\n   - Spam olmaz \n\n 👉 **ASİSTANT SİZİN QRUPUNUZA QATILA BİLMƏSƏ, QRUP LİNKİNİ GÖNDƏRİN.**\n\n ⚠️ Diqqət: Buraya bir mesaj göndərirsinizsə, demək Sahibim mesajınızı görəcək və məni söhbətə qatacaq\n    - Bu istifadəçini gizli qruplara əlavə etməyin.\n   - Şəxsi məlumatları burada paylaşmayın\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pm aktivləşdirildi")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pm söndürüldü")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Mesaj göndərilməsi səbəbindən PM təsdiq edildi")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("PM icazəsi aktivləşdirildi")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("PM deaktiv edildi")
        return
    message.continue_propagation()
