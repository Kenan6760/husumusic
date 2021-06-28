from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from DaisyXMusic.helpers.decorators import authorized_users_only
from DaisyXMusic.helpers.decorators import errors
from DaisyXMusic.services.callsmusic import client as USER
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["add"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Əvvəlcə məni qrupunuza admin kimi əlavə edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Brend Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "İstədiyiniz kimi buraya qoşuldum🥳")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Onsuz da asistant qrupunuzda var🥴</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Xəta BAş Verdi 🛑 \n {user.first_name} Asistant qrupunuzda ban olunduğuna görə qrupunuza qoşula bilmədi! Asistantın banını açıb yenidən yoxlayın"
            "\n\nVə ya özünüz @BrendMusicAsistant qrupa əlavə edin və yenidən cəhd edin</b>",
        )
        return
    await message.reply_text(
        "<b>Asistant Söhbətinizə qatıldı✅</b>",
    )


@USER.on_message(filters.group & filters.command(["leave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>İstifadəçi qrupunuzdan çıxa bilmədi! Xəta."
            "\n\nYa da məni Qrupunuzdan /kick edərək çıxarınb>",
        )
        return
    
@Client.on_message(filters.command(["leaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Asistant Bütün söhbətləri tərk edir")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Asistant qruplardan ayrılır... Ayrılır: {left} söhbətlər. Uğursuz oldu: {failed} söhbət.")
            except:
                failed=failed+1
                await lol.edit(f"Asistant qruuplardan ayrılır... Ayrıldı: {left} söhbətdən. Uğursuz oldu: {failed} söhbət.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Ayrıldı: {left} söhbətdən. {falied} söhbətdən ayrılmadı.")
    
    
@Client.on_message(filters.command(["addchannel","addchnl"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Söhbət hətta bağlıdır")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Əvvəlcə məni kanalınızın admini kimi əlavə edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Brend Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "İstədiyiniz kimi buraya qoşuldum")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistant onsuz da kanalınızdadır</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Xəta Baş Verdi 🛑 \n User {user.first_name} Asistant kanalınızda ban olunduğuna görə qoşula bilmədi! Asistantın kanalda ban olunmadığından əmin olun."
            "\n\nVə ya Qrupunuza @BrendMusicAsistant əl ilə əlavə edin və yenidən cəhd edin</b>",
        )
        return
    await message.reply_text(
        "<b>Asistant kanalınıza qatıldı</b>",
    )
    
