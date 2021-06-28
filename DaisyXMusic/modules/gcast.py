from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("Yayım Başladı")
        if not message.reply_to_message:
            await lol.edit("Yayımlamaq üçün hər hansısa bir mətn mesajına cavab verin")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"Yayım Tamamlandı✅ Göndərildi: {sent} söhbətlər. Uğursuz oldu: {failed} söhbət.")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                await lol.edit(f"Yayım Tamamlandı✅ Göndərildi: {sent} söhbətlər. Uğursuz oldu: {failed} söhbət.")
                await asyncio.sleep(0.7)
                
        await message.reply_text(f"Yayım Tamamlandı✅ Göndərildi: {sent} söhbətlər. Uğursuz oldu: {failed} söhbət.")
