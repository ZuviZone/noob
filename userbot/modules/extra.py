import asyncio, subprocess
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from lmgtfy import lmgtfy
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.modules.rextester.api import UnknownLanguage, Rextester

@register(outgoing=True, pattern="^.leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Group kek!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sar This is Not A Chat`')

@register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@register(outgoing=True, pattern="^Ook$")
async def Ook(e):
    t = "Ook"
    for j in range(15):
        t = t[:-1] + "ok"
        await e.edit(t)
	
@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@register(outgoing=True, pattern="^.moon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/noobanon/noob/")

@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/noobanon/noob/blob/master/README.md")

@register(outgoing=True, pattern="^.dis$")
async def disapprovepm(disapprvpm):
    if not disapprvpm.text[0].isalpha() and disapprvpm.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import dissprove
        except:
            await disapprvpm.edit("`Running on Non-SQL mode!`")
            return

        if disapprvpm.reply_to_msg_id:
            reply = await disapprvpm.get_reply_message()
            replied_user = await bot(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            dissprove(replied_user.user.id)
        else:
            dissprove(disapprvpm.chat_id)
            aname = await bot.get_entity(disapprvpm.chat_id)
            name0 = str(aname.first_name)

        await disapprvpm.edit(
            f"[{name0}](tg://user?id={disapprvpm.chat_id}) `Disaproved to PM! nikal lavde `"
            )

        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                f"[{name0}](tg://user?id={disapprvpm.chat_id})"
                " was disapproved to PM you nikal lavde.",
            )

@register(outgoing=True, pattern="^.clock$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@register(outgoing=True, pattern="^.myusernames$")
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)

@register(outgoing=True, pattern="^\$")
async def rextestercli(e):
    stdin = ""
    message = e.text
    chat = await e.get_chat()

    if len(message.split()) > 1:
        regex = re.search(
            r"^\$([\w.#+]+)\s+([\s\S]+?)(?:\s+\/stdin\s+([\s\S]+))?$",
            message,
            re.IGNORECASE,
        )
        language = regex.group(1)
        code = regex.group(2)
        stdin = regex.group(3)

        try:
            rextester = Rextester(language, code, stdin)
            res = await rextester.exec()
        except UnknownLanguage as exc:
            await e.edit(str(exc))
            return

        output = ""
        output += f"**Language:**\n```{language}```"
        output += f"\n\n**Source:** \n```{code}```"

        if res.result:
            output += f"\n\n**Result:** \n```{res.result}```"

        if res.warnings:
            output += f"\n\n**Warnings:** \n```{res.warnings}```\n"

        if res.errors:
            output += f"\n\n**Errors:** \n'```{res.errors}```"

        if len(res.result) > 4096:
            with io.BytesIO(str.encode(res.result)) as out_file:
                out_file.name = "result.txt"
                await bot.send_file(chat.id, file = out_file)
                await e.edit(code)
            return

        await e.edit(output)


CMD_HELP.update({
    "leave": "Leave a Chat"
})
CMD_HELP.update({
    ";__;": "You try it!"
})
CMD_HELP.update({
    "cry": "Cry"
})
CMD_HELP.update({
    "fp": "Send face palm emoji."
})
CMD_HELP.update({
    "moon": "Bot will send a cool moon animation."
})
CMD_HELP.update({
    "clock": "Bot will send a cool clock animation."
})
CMD_HELP.update({
    "readme": "Reedme."
})
CMD_HELP.update({
    "sauce": "source."
})
CMD_HELP.update({
    "dis": "Disapprove anyone in PM."
})
CMD_HELP.update({
    "myusernames": "List of Usernames owned by you."
})
CMD_HELP.update({
    "oof": "Same as ;__; but ooof"
})
CMD_HELP.update({
    "ook": "Same as ;__; but oook"
})
