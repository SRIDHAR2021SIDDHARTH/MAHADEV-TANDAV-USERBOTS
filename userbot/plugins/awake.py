
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/8eff616d2c2a262304969.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱𝕄𝔸ℍ𝔸𝔻𝔼𝕍 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝕀𝕊 𝔸𝕎𝔸𝕂𝔼..🔱 \n\n\n**"
   ALIVE_MESSAGE += "`ꜱᴛᴀᴛꜱ \n\n\n`"
   ALIVE_MESSAGE += f"`ᴛᴇʟᴇᴛʜᴏɴ: TELETHON-1.19.0 \n\n`"
   ALIVE_MESSAGE += f"`ᴘʏᴛʜᴏɴ: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`ɪ'ʟʟ ʙᴇ ᴡɪᴛʜ ʏᴏᴜ ᴍᴀꜱᴛᴇʀ ᴛɪʟʟ ᴍʏ ᴅʏɴᴏ ᴇɴᴅꜱ ᴏʀ ʏᴏᴜ ꜱᴡɪᴛᴄʜ ᴏꜰꜰ ᴍᴇ ᴍᴀɴᴜᴀʟʟʏ!☠ \n\n`"
   ALIVE_MESSAGE += f"`ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ` :  @TANDAV_USERBOT_CHANNEL\n\n"
   ALIVE_MESSAGE += f"`ꜱᴜᴘᴘᴏʀᴛ/ꜱᴜɢɢᴇꜱᴛɪᴏɴ ɢʀᴏᴜᴘ` :  @TANDAV_USERBOT_SUPPORT\n\n"
   ALIVE_MESSAGE += f"`ᴍʏ ᴘᴇʀᴏᴏ ꜱᴇ ʙʜɪ ᴘᴇʀᴏᴏ ᴍᴀꜱᴛᴇʀ🔥`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
