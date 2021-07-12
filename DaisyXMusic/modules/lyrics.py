import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("🔎Sözləri axtarırıq.....")
    query = message.text
    if not query:
        await lel.edit("`🤨Nəyi tapmalıyam? `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "😔Bu mahnının sözlərini tapa bilmədim! Bəlkə mahnı ilə yanaşı oxuyanın adınıda yazasan?🤔. .glyrics`"
    else:
        reply = "sözləri tapılmadı! hələ çalışmırsa mahnı ilə yanaşı sənətçi adı ilə də cəhd edin. .glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "sözlər.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)
