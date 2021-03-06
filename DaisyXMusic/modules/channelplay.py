import json
from os import path
from typing import Callable

import aiofiles
import aiohttp
import ffmpeg
import requests
import wget
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pyrogram import Client 
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import Voice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Python_ARQ import ARQ
from youtube_search import YoutubeSearch
from DaisyXMusic.modules.play import generate_cover
from DaisyXMusic.modules.play import arq
from DaisyXMusic.modules.play import cb_admin_check
from DaisyXMusic.modules.play import transcode
from DaisyXMusic.modules.play import convert_seconds
from DaisyXMusic.modules.play import time_to_seconds
from DaisyXMusic.modules.play import changeImageSize
from DaisyXMusic.config import BOT_NAME as bn
from DaisyXMusic.config import DURATION_LIMIT
from DaisyXMusic.config import UPDATES_CHANNEL as updateschannel
from DaisyXMusic.config import que
from DaisyXMusic.function.admins import admins as a
from DaisyXMusic.helpers.errors import DurationLimitError
from DaisyXMusic.helpers.decorators import errors
from DaisyXMusic.helpers.admins import get_administrators
from DaisyXMusic.helpers.channelmusic import get_chat_id
from DaisyXMusic.helpers.decorators import authorized_users_only
from DaisyXMusic.helpers.filters import command
from DaisyXMusic.helpers.filters import other_filters
from DaisyXMusic.helpers.gets import get_file_name
from DaisyXMusic.services.callsmusic import callsmusic
from DaisyXMusic.services.callsmusic import client as USER
from DaisyXMusic.services.converter.converter import convert
from DaisyXMusic.services.downloaders import youtube
from DaisyXMusic.services.queues import queues

chat_id = None


@Client.on_message(filters.command(["channelplaylist","cplaylist"]) & filters.group & ~filters.edited)
async def playlist(client, message):
    try:
      lel = await client.get_chat(message.chat.id)
      lol = lel.linked_chat.id
    except:
      message.reply("Bu pi??ik h??tta ??laq??lidir?")
      return
    global que
    queue = que.get(lol)
    if not queue:
        await message.reply_text("Asistant bo??dur")
    temp = []
    for t in queue:
        temp.append(t)
    now_playing = temp[0][0]
    by = temp[0][1].mention(style="md")
    msg = "<b>??ndi oxunur</b> in {}".format(lel.linked_chat.title)
    msg += "\n- " + now_playing
    msg += "\n- ??st??di " + by
    temp.pop(0)
    if temp:
        msg += "\n\n"
        msg += "<b>N??vb??</b>"
        for song in temp:
            name = song[0]
            usr = song[1].mention(style="md")
            msg += f"\n- {name}"
            msg += f"\n- ??st??di {usr}\n"
    await message.reply_text(msg)


# ============================= Settings =========================================


def updated_stats(chat, queue, vol=100):
    if chat.id in callsmusic.active_chats:
        # if chat.id in active_chats:
        stats = "**{}** parametrl??ri".format(chat.title)
        if len(que) > 0:
            stats += "\n\n"
            stats += "S??s : {}%\n".format(vol)
            stats += "Qrupda ??al??nan mahn?? say?? : `{}`\n".format(len(que))
            stats += "??ndi oxunur : **{}**\n".format(queue[0][0])
            stats += "??st??di : {}".format(queue[0][1].mention)
    else:
        stats = None
    return stats


def r_ply(type_):
    if type_ == "play":
        pass
    else:
        pass
    mar = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("???", "cleave"),
                InlineKeyboardButton("???", "cpuse"),
                InlineKeyboardButton("??????", "cresume"),
                InlineKeyboardButton("???", "cskip"),
            ],
            [
                InlineKeyboardButton("Playlist ????", "cplaylist"),
            ],
            [InlineKeyboardButton("??? Ba??la", "ccls")],
        ]
    )
    return mar


@Client.on_message(filters.command(["channelcurrent","ccurrent"]) & filters.group & ~filters.edited)
async def ee(client, message):
    try:
      lel = await client.get_chat(message.chat.id)
      lol = lel.linked_chat.id
      conv = lel.linked_chat
    except:
      await message.reply("S??hb??t linki ba??l??d??r")
      return
    queue = que.get(lol)
    stats = updated_stats(conv, queue)
    if stats:
        await message.reply(stats)
    else:
        await message.reply("Bu s??hb??td?? s??sli S??hb??t yoxdur")


@Client.on_message(filters.command(["channelplayer","cplayer"]) & filters.group & ~filters.edited)
@authorized_users_only
async def settings(client, message):
    playing = None
    try:
      lel = await client.get_chat(message.chat.id)
      lol = lel.linked_chat.id
      conv = lel.linked_chat
    except:
      await message.reply("S??hb??t linki ba??l??d??r")
      return
    queue = que.get(lol)
    stats = updated_stats(conv, queue)
    if stats:
        if playing:
            await message.reply(stats, reply_markup=r_ply("pause"))

        else:
            await message.reply(stats, reply_markup=r_ply("play"))
    else:
        await message.reply("Bu s??hb??td?? s??sli S??hb??t yoxdur")


@Client.on_callback_query(filters.regex(pattern=r"^(cplaylist)$"))
async def p_cb(b, cb):
    global que
    try:
      lel = await client.get_chat(cb.message.chat.id)
      lol = lel.linked_chat.id
      conv = lel.linked_chat
    except:
      return    
    que.get(lol)
    type_ = cb.matches[0].group(1)
    cb.message.chat.id
    cb.message.chat
    cb.message.reply_markup.inline_keyboard[1][0].callback_data
    if type_ == "playlist":
        queue = que.get(lol)
        if not queue:
            await cb.message.edit("Asistant bo??dur")
        temp = []
        for t in queue:
            temp.append(t)
        now_playing = temp[0][0]
        by = temp[0][1].mention(style="md")
        msg = "**??ndi oxunur** in {}".format(conv.title)
        msg += "\n- " + now_playing
        msg += "\n- ??st??di " + by
        temp.pop(0)
        if temp:
            msg += "\n\n"
            msg += "**N??vb??**"
            for song in temp:
                name = song[0]
                usr = song[1].mention(style="md")
                msg += f"\n- {name}"
                msg += f"\n- ??st??di {usr}\n"
        await cb.message.edit(msg)


@Client.on_callback_query(
    filters.regex(pattern=r"^(cplay|cpause|cskip|cleave|cpuse|cresume|cmenu|ccls)$")
)
@cb_admin_check
async def m_cb(b, cb):
    global que
    if (
        cb.message.chat.title.startswith("Channel Music: ")
        and chat.title[14:].isnumeric()
    ):
        chet_id = int(chat.title[13:])
    else:
      try:
        lel = await b.get_chat(cb.message.chat.id)
        lol = lel.linked_chat.id
        conv = lel.linked_chat
        chet_id = lol
      except:
        return
    qeue = que.get(chet_id)
    type_ = cb.matches[0].group(1)
    cb.message.chat.id
    m_chat = cb.message.chat
    

    the_data = cb.message.reply_markup.inline_keyboard[1][0].callback_data
    if type_ == "cpause":
        if (chet_id not in callsmusic.active_chats) or (
            callsmusic.active_chats[chet_id] == "paused"
        ):
            await cb.answer("S??hb??t?? ba??lan??lmay??b!", show_alert=True)
        else:
            callsmusic.pause(chet_id)
            await cb.answer("Musiqi dayand??r??ld??!")
            await cb.message.edit(
                updated_stats(conv, qeue), reply_markup=r_ply("play")
            )

    elif type_ == "cplay":
        if (chet_id not in callsmusic.active_chats) or (
            callsmusic.active_chats[chet_id] == "playing"
        ):
            await cb.answer("S??hb??t?? ba??lan??lmay??b!", show_alert=True)
        else:
            callsmusic.resume(chet_id)
            await cb.answer("Musiqi Davam edir!")
            await cb.message.edit(
                updated_stats(conv, qeue), reply_markup=r_ply("pause")
            )

    elif type_ == "cplaylist":
        queue = que.get(cb.message.chat.id)
        if not queue:
            await cb.message.edit("Asistant bo??dur")
        temp = []
        for t in queue:
            temp.append(t)
        now_playing = temp[0][0]
        by = temp[0][1].mention(style="md")
        msg = "**??ndi Oxunur** in {}".format(cb.message.chat.title)
        msg += "\n- " + now_playing
        msg += "\n- ??st??di " + by
        temp.pop(0)
        if temp:
            msg += "\n\n"
            msg += "**N??vb??**"
            for song in temp:
                name = song[0]
                usr = song[1].mention(style="md")
                msg += f"\n- {name}"
                msg += f"\n- ??st??di {usr}\n"
        await cb.message.edit(msg)

    elif type_ == "cresume":
        if (chet_id not in callsmusic.active_chats) or (
            callsmusic.active_chats[chet_id] == "playing"
        ):
            await cb.answer("S??hb??t?? ba??lanmay??b v?? ya art??q oxunur", show_alert=True)
        else:
            callsmusic.resume(chet_id)
            await cb.answer("Musiqi davam edir!")
    elif type_ == "cpuse":
        if (chet_id not in callsmusic.active_chats) or (
            callsmusic.active_chats[chet_id] == "paused"
        ):
            await cb.answer("Chat is not connected or already paused", show_alert=True)
        else:
            callsmusic.pause(chet_id)
            await cb.answer("Musiqi dayand??r??ld??!")
    elif type_ == "ccls":
        await cb.answer("Menyunu Ba??la")
        await cb.message.delete()

    elif type_ == "cmenu":
        stats = updated_stats(conv, qeue)
        await cb.answer("Menyunu a??")
        marr = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("???", "cleave"),
                    InlineKeyboardButton("???", "cpuse"),
                    InlineKeyboardButton("??????", "cresume"),
                    InlineKeyboardButton("???", "cskip"),
                ],
                [
                    InlineKeyboardButton("Playlist ????", "cplaylist"),
                ],
                [InlineKeyboardButton("??? Ba??la", "ccls")],
            ]
        )
        await cb.message.edit(stats, reply_markup=marr)
    elif type_ == "cskip":
        if qeue:
            qeue.pop(0)
        if chet_id not in callsmusic.active_chats:
            await cb.answer("S??hb??t?? ba??lan??lmay??b!", show_alert=True)
        else:
            queues.task_done(chet_id)

            if queues.is_empty(chet_id):
                callsmusic.stop(chet_id)
                await cb.message.edit("- Art??q pleylist yoxdur..\n- S??sli s??hb??td??n ????x??r??q!")
            else:
                await callsmusic.set_stream(
                    chet_id, queues.get(chet_id)["file"]
                )
                await cb.answer.reply_text("??? <b>N??vb??tiy?? ke??irildi</b>")
                await cb.message.edit((m_chat, qeue), reply_markup=r_ply(the_data))
                await cb.message.reply_text(
                    f"- ??ndi oxunur **{qeue[0][0]}**\n- N??vb??ti mahn??"
                )

    else:
        if chet_id in callsmusic.active_chats:
            try:
               queues.clear(chet_id)
            except QueueEmpty:
                pass

            callsmusic.stop(chet_id)
            await cb.message.edit("S??hb??ti u??urla t??rk etdim!")
        else:
            await cb.answer("S??hb??t?? ba??lanmay??b!", show_alert=True)


@Client.on_message(filters.command(["channelplay","cplay"])  & filters.group & ~filters.edited)
@authorized_users_only
async def play(_, message: Message):
    global que
    lel = await message.reply("???? <b>Proses ba??lan??ld??</b>")

    try:
      conchat = await _.get_chat(message.chat.id)
      conv = conchat.linked_chat
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("S??hb??t linki ba??l??d??r")
      return
    try:
      administrators = await get_administrators(conv)
    except:
      await message.reply("Kanalda m??ni admin edin")
    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"
    usar = user
    wew = usar.id
    try:
        # chatdetails = await USER.get_chat(chid)
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                if message.chat.title.startswith("Kanal Musiqisi: "):
                    await lel.edit(
                        "<b>Kanal??n??za asistant?? ??lav?? etm??yi unutmay??n</b>",
                    )
                    pass

                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>??nc?? m??ni kanal??n??z??n admini kimi ??lav?? edin</b>",
                    )
                    return

                try:
                    await USER.join_chat(invitelink)
                    await lel.edit(
                        "<b>Asistant kanal??n??za qat??ld??</b>",
                    )

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    # print(e)
                    await lel.edit(
                        f"<b>???? X??ta Ba?? verdi ???? \n {user.first_name} Asistant kanalda ban olundu??una g??r?? qat??la bilmir! Asistant??n kanalda banlanmad??????ndan ??min olun."
                        "\n\nV?? ya ??linizl?? qrupunuza @BrendMusicAsistant ??lav?? edin v?? yenid??n c??hd edin</b>",
                    )
    try:
        await USER.get_chat(chid)
        # lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"<i> {user.first_name} Asistant s??hb??td?? yoxdur, Kanalda hans??sa adminin /play ??mrini verib mahn?? oxutmas??n?? v?? ya /add yaz??b {user.first_name} Asistant?? ??lav?? etm??sini ist??</i>"
        )
        return
    message.from_user.id
    text_links = None
    message.from_user.first_name
    await lel.edit("???? <b>Axtar??l??r</b>")
    message.from_user.id
    user_id = message.from_user.id
    message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    if message.reply_to_message:
        entities = []
        toxt = message.reply_to_message.text or message.reply_to_message.caption
        if message.reply_to_message.entities:
            entities = message.reply_to_message.entities + entities
        elif message.reply_to_message.caption_entities:
            entities = message.reply_to_message.entities + entities
        urls = [entity for entity in entities if entity.type == 'url']
        text_links = [
            entity for entity in entities if entity.type == 'text_link'
        ]
    else:
        urls=None
    if text_links:
        urls = True    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            await lel.edit(
                f"??? {DURATION_LIMIT} d??qiq??d??n uzun s??sl??rin oxudulamas??na icaz?? verilmir!"
            )
            return
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("???? Playlist", callback_data="cplaylist"),
                    InlineKeyboardButton("Menu ??? ", callback_data="cmenu"),
                ],
                [InlineKeyboardButton(text="??? Ba??la", callback_data="ccls")],
            ]
        )
        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/25345dfb9e0d27909b9be.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Yerli olaraq ??lav?? edildi"
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )
    elif urls:
        query = toxt
        await lel.edit("???? **Proses ba??lad??l??r**")
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"][:40]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            results[0]["url_suffix"]
            views = results[0]["views"]

        except Exception as e:
            await lel.edit(
                "Mahn?? tap??lmad??. Ba??qa bir mahn??n?? s??nay??n v?? ya ad??n?? d??zg??n yaz??n."
            )
            print(str(e))
            return
        try:    
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
            if (dur / 60) > DURATION_LIMIT:
                 await lel.edit(f"??? {DURATION_LIMIT} d??qiq??d??n uzun s??sl??rin oxudulmas??na icaz?? verilmir!")
                 return
        except:
            pass        
        dlurl = url
        dlurl=dlurl.replace("youtube","youtubepp")
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Burada sizin Reklam??n??z ola bil??rdi?????????????????", url=f"t.me/brend_reklam"),
                ],
                [
                    InlineKeyboardButton("???? Playlist", callback_data="cplaylist"),
                    InlineKeyboardButton("Menu ??? ", callback_data="cmenu"),
                ],
                [
                    InlineKeyboardButton(text="???? YouTube", url=f"{url}"),
                    InlineKeyboardButton(text="D??st??k ????", url=f"t.me/brendsup"),
                ],
                [InlineKeyboardButton(text="??? Ba??la", callback_data="ccls")],
            ]
        )
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await convert(youtube.download(url))        
    else:
        query = ""
        for i in message.command[1:]:
            query += " " + str(i)
        print(query)
        await lel.edit("???? **Proses Ba??lad??l??r**")
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"][:40]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            results[0]["url_suffix"]
            views = results[0]["views"]

        except Exception as e:
            await lel.edit(
                "Mahn?? tap??lmad??. Ba??qa bir mahn??n?? s??nay??n v?? ya ad??n?? d??zg??n yaz??n."
            )
            print(str(e))
            return
        try:    
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
            if (dur / 60) > DURATION_LIMIT:
                 await lel.edit(f"??? {DURATION_LIMIT} uzun s??sl??rin oxudulmas??na icaz?? verilmir!")
                 return
        except:
            pass
        dlurl = url
        dlurl=dlurl.replace("youtube","youtubepp")
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Burada sizin Reklam??n??z ola bil??rdi?????????????????", url=f"t.me/brend_reklam"),
                ],
                [
                    InlineKeyboardButton("???? Playlist", callback_data="cplaylist"),
                    InlineKeyboardButton("Menu ??? ", callback_data="cmenu"),
                ],
                [
                    InlineKeyboardButton(text="???? YouTube", url=f"{url}"),
                    InlineKeyboardButton(text="D??st??k ????", url=f"t.me/brendsup"),
                ],
                [InlineKeyboardButton(text="??? Ba??la", callback_data="ccls")],
            ]
        )
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await convert(youtube.download(url))
    chat_id = chid
    if chat_id in callsmusic.active_chats:
        position = await queues.put(chat_id, file=file_path)
        qeue = que.get(chat_id)
        s_name = title
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await message.reply_photo(
            photo="final.png",
            caption=f"#???{position} Sizin mahn??n??z n??mr??l??n??r??k <b>n??vb??y?? al??nd??</b>!",
            reply_markup=keyboard,
        )
        os.remove("final.png")
        return await lel.delete()
    else:
        chat_id = chid
        que[chat_id] = []
        qeue = que.get(chat_id)
        s_name = title
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await callsmusic.set_stream(chat_id, file_path)
        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="??????{} <b>T??r??find??n</b> sifari?? olunan musiqi s??sli s??hb??td?? oxunur".format(
                message.from_user.mention()
            ),
        )
        os.remove("final.png")
        return await lel.delete()


@Client.on_message(filters.command(["channeldplay","cdplay"]) & filters.group & ~filters.edited)
@authorized_users_only
async def deezer(client: Client, message_: Message):
    global que
    lel = await message_.reply("???? <b>Proses ba??lad??l??r</b>")

    try:
      conchat = await client.get_chat(message_.chat.id)
      conid = conchat.linked_chat.id
      conv = conchat.linked_chat
      chid = conid
    except:
      await message_.reply("S??hb??t linki ba??l??d??r")
      return
    try:
      administrators = await get_administrators(conv)
    except:
      await message.reply("M??ni Kanalda admin edin") 
    try:
        user = await USER.get_me()
    except:
        user.first_name = "Brend Music"
    usar = user
    wew = usar.id
    try:
        # chatdetails = await USER.get_chat(chid)
        await client.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message_.from_user.id:
                if message_.chat.title.startswith("Kanal Musiqisi: "):
                    await lel.edit(
                        "<b>Kanal??n??za Asistant?? ??lav?? etm??yi unutmay??n</b>",
                    )
                    pass
                try:
                    invitelink = await client.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>??nc?? m??ni kanal??n??z??n admini kimi ??lav?? edin</b>",
                    )
                    return

                try:
                    await USER.join_chat(invitelink)
                    await lel.edit(
                        "<b>Asistant kanal??n??za qat??ld??</b>",
                    )

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    # print(e)
                    await lel.edit(
                        f"<b>???? X??ta Ba?? verdi ???? \n {user.first_name} Asistant kanalda ban olundu??una g??r?? qat??la bilmir! Asistant??n kanalda banlanmad??????ndan ??min olun."
                        "\n\nV?? ya ??linizl?? qrupunuza @BrendMusicAsistant ??lav?? edin v?? yenid??n c??hd edin</b>",
                    )
    try:
        await USER.get_chat(chid)
        # lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"<i> {user.first_name} Asistant bu kanalda yoxdur, admind??n ilk d??f?? /play ??mrini g??nd??rm??sini v?? mahn?? oxutmas??n?? ist??yin v?? ya {user.first_name} -i ??l il?? ??lav?? edin</i>"
        )
        return
    requested_by = message_.from_user.first_name

    text = message_.text.split(" ", 1)
    queryy = text[1]
    query=queryy
    res = lel
    await res.edit(f"Deezer-d?? `{queryy}` ??????n ???? axtar???? apar??l??r")
    try:
        songs = await arq.deezer(query,1)
        if not songs.ok:
            await message_.reply_text(songs.result)
            return
        title = songs.result[0].title
        url = songs.result[0].url
        artist = songs.result[0].artist
        duration = songs.result[0].duration
        thumbnail = songs.result[0].thumbnail
    except:
        await res.edit("S??z??n ??sl m??nas??nda he?? bir ??ey tap??lmad??, ??ngilis dilind?? i??l??m??lis??n!")
        return
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("???? Playlist", callback_data="cplaylist"),
                InlineKeyboardButton("Menu ??? ", callback_data="cmenu"),
            ],
            [InlineKeyboardButton(text="Listen On Deezer ????", url=f"{url}")],
            [InlineKeyboardButton(text="??? Ba??la", callback_data="ccls")],
        ]
    )
    file_path = await convert(wget.download(url))
    await res.edit("Generating Thumbnail")
    await generate_cover(requested_by, title, artist, duration, thumbnail)
    chat_id = chid
    if chat_id in callsmusic.active_chats:
        await res.edit("adding in queue")
        position = await queues.put(chat_id, file=file_path)
        qeue = que.get(chat_id)
        s_name = title
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await res.edit_text(f"???{bn}???= #?????? {Position} m??vqeyind?? n??vb??y?? al??nd??")
    else:
        await res.edit_text(f"???{bn}???=?????? Oxunur.....")

        que[chat_id] = []
        qeue = que.get(chat_id)
        s_name = title
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
    await callsmusic.set_stream(chat_id, file_path)
    await res.delete()

    m = await client.send_photo(
        chat_id=message_.chat.id,
        reply_markup=keyboard,
        photo="final.png",
        caption=f"Ba??l?? Kanalda Deezer vasit??sil?? [{title}]({url}) ??al??n??r",
    )
    os.remove("final.png")


@Client.on_message(filters.command(["channelsplay","csplay"]) & filters.group & ~filters.edited)
@authorized_users_only
async def jiosaavn(client: Client, message_: Message):
    global que
    lel = await message_.reply("???? **Proses ba??lad??l??r**")
    try:
      conchat = await client.get_chat(message_.chat.id)
      conid = conchat.linked_chat.id
      conv = conchat.linked_chat
      chid = conid
    except:
      await message_.reply("S??hb??t h??tta ba??l??d??r")
      return
    try:
      administrators = await get_administrators(conv)
    except:
      await message.reply("M??ni kanalda admin edin")
    try:
        user = await USER.get_me()
    except:
        user.first_name = "Brend Music"
    usar = user
    wew = usar.id
    try:
        # chatdetails = await USER.get_chat(chid)
        await client.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message_.from_user.id:
                if message_.chat.title.startswith("Channel Music: "):
                    await lel.edit(
                        "<b>Kanal??n??za Asistant ??lav?? etm??yi unutmay??n</b>",
                    )
                    pass
                try:
                    invitelink = await client.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>??vv??lc?? m??ni qrupunuzun admini kimi ??lav?? edin</b>",
                    )
                    return

                try:
                    await USER.join_chat(invitelink)
                    await lel.edit(
                        "<b>Asistant kanal??n??za qat??ld??</b>",
                    )

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    # print(e)
                    await lel.edit(
                        f"<b>???? X??ta Ba?? verdi ???? \n {user.first_name} Asistant kanalda ban olundu??una g??r?? qat??la bilmir! Asistant??n kanalda banlanmad??????ndan ??min olun."
                        "\n\nV?? ya ??linizl?? qrupunuza @BrendMusicAsistant ??lav?? edin v?? yenid??n c??hd edin</b>",
                    )
    try:
        await USER.get_chat(chid)
        # lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            "<i> Asistant bu kanalda yoxdur, admind??n ilk d??f?? /play ??mrini g??nd??rm??sini v?? mahn?? oxutmas??n?? ist??yin v?? ya {user.first_name} -i ??l il?? ??lav?? edin</i>"
        )
        return
    requested_by = message_.from_user.first_name
    chat_id = message_.chat.id
    text = message_.text.split(" ", 1)
    query = text[1]
    res = lel
    await res.edit(f"Jio saavn-d?? `{query}` ??????n ???? axtar???? apar??l??r")
    try:
        songs = await arq.saavn(query)
        if not songs.ok:
            await message_.reply_text(songs.result)
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        sthumb = "https://telegra.ph/file/f6086f8909fbfeb0844f2.png"
        sduration = int(songs.result[0].duration)
    except Exception as e:
        await res.edit("He?? bir ??ey tap??lmad??! ??ngilis dilind?? i??l??m??lis??n")
        print(str(e))
        return
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("???? Playlist", callback_data="cplaylist"),
                InlineKeyboardButton("Menu ??? ", callback_data="cmenu"),
            ],
            [
                InlineKeyboardButton(
                    text="Yenil??m??l??r Kanal??na qo??ulun", url=f"https://t.me/{updateschannel}"
                )
            ],
            [InlineKeyboardButton(text="??? Ba??la", callback_data="ccls")],
        ]
    )
    file_path = await convert(wget.download(slink))
    chat_id = chid
    if chat_id in callsmusic.active_chats:
        position = await queues.put(chat_id, file=file_path)
        qeue = que.get(chat_id)
        s_name = sname
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await res.delete()
        m = await client.send_photo(
            chat_id=message_.chat.id,
            reply_markup=keyboard,
            photo="final.png",
            caption=f"???{bn}???=#?????? {position} m??vqeyind?? n??vb??y?? al??nd??",
        )

    else:
        await res.edit_text(f"{bn}=?????? Oxunur.....")
        que[chat_id] = []
        qeue = que.get(chat_id)
        s_name = sname
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
    await callsmusic.set_stream(chat_id, file_path)
    await res.edit("Ki??ik ????kil yarad??r.")
    await generate_cover(requested_by, sname, ssingers, sduration, sthumb)
    await res.delete()
    m = await client.send_photo(
        chat_id=message_.chat.id,
        reply_markup=keyboard,
        photo="final.png",
        caption=f"Ba??l?? kanalda {sname} Via Jiosaavn oynan??r",
    )
    os.remove("final.png")
