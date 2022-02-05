# Thanks to @Shivam_Patel Bro
# Thanks to Sipak .. 
# Idea by @Shivam_Patel 
# Made by @Shivam_Patel & @ProgrammingError ....TEAM DC
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from userbot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
        dc_text=(f"** MAHADEV TORNADO 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n✘ About My System ✘\n\n➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/MAHADEV_TORNADO_USERBOT_SUPPORT)\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝙏𝙚𝙖𝙢 MT](https://github.com/SRIDHAR2021SIDDHARTH)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [Mahadev-Tornado](https://github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS)\n\n➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS/blob/master")],
                    [Button.url("String", "https://replit.com/@TANDAVSIDDHARTH/TANDAV-USERBOT#main.py"),
                    Button.url("Channel", "https://t.me/MAHADEV_TORNADO_USERBOT_OFFICIAL"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="DARK Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Dark Cobra",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
