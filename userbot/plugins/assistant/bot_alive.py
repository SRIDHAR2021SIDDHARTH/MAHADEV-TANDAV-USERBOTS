from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸ℍ𝔸𝔻𝔼𝕍 TORNADO 𝕌𝕊𝔼ℝ𝔹𝕆𝕋"
PM_IMG = "https://telegra.ph/file/6f739e51ecfc6bf7ee9de.jpg"
pm_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.8.6` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `2.0`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOTS/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [𝕄𝔸ℍ𝔸𝔻𝔼𝕍 TORNADO 𝕌𝕊𝔼ℝ𝔹𝕆𝕋](https://t.me/MAHADEV_TORNADO_USERBOT_OFFICIAL)\n"
pm_caption += "[Assistant By 𝕄𝔸ℍ𝔸𝔻𝔼𝕍 TORNADO 𝕌𝕊𝔼ℝ𝔹𝕆𝕋](https://t.me/MAHADEV_TORNADO_USERBOT_SUPPORT)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
