# Thanks To JassManak1125 For adding few more edits..

# Added some new edits..

# Got it from @userbotjunks
# All in one code.

"""
Available Commands:
.tlol
.lol
.heart
.candy
.nothappy"""

from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"candy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😁☹️😁☹️😁☹️😁"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"heart"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"ethink"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤨🤔🧐🤨"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("😂🤣😂🤣😂🤣"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
        
from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"lund"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍆🖕🏻🍆🖕🏻🍆🖕🏻"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
   
from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"bsdk"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🙄😑😤🖕🏻🙄😑😤🖕🏻"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)		
		
@borg.on(admin_cmd(pattern=r"phukk"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("T3RI MAAKI CHUT"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)		
		
@borg.on(admin_cmd(pattern=r"mahadev"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🔱HAR HAR MAHAD3V🔱"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern=r"repo"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("https://github.com/SRIDHAR2021SIDDHARTH/MAHADEV-TANDAV-USERBOT"))
	for _ in range(20):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
			

