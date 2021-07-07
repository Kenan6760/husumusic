import asyncio

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant

from DaisyXMusic.services.callsmusic.callsmusic import client as USER
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Yayım başlayır✅...`")
        if not message.reply_to_message:
            await wtf.edit("Xahiş edirəm yayımlanacaq bir mesajı cavablandırın!🥴")
            return
        lmao = message.reply_to_message.text
        async for dialog in USER.iter_dialogs():
            try:
                await USER.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`🌐Yayımlanır🔄...` \n\n**Göndərildi:** `{sent}` Söhbətə \n**Uğursuz oldu:** {failed} Söhbətdə")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                await wtf.edit(f"`🌐Yayımlanır🔄...` \n\n**Göndərildi:** `{sent}` Söhbətə \n**Uğursuz oldu:** {failed} Söhbətdə")
                
            
        await message.reply_text(f"`✅Yayım bitdi🥳` \n\n**Göndərildi:** `{sent}` Söhbətə \n**Uğursuz oldu:** {failed} Söhbətdə")
