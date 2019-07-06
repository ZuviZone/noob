# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
#

""" Userbot module for having some fun. """

import asyncio
import random
import re
import time

from spongemock import spongemock
from zalgo_text import zalgo

from cowpy import cow

from userbot import (DISABLE_RUN, WIDE_MAP, CMD_HELP)
from userbot.events import register

# ================= CONSTANT =================
METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
]
EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]
UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]
FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]
RUNSREACTS = [
    "`Ye Bedard Zamana Kya Jane, Kya Cheez Judayi Hoti Hai, Hum L*nd Pakad Kar Sote Hai, Ghar Ghar Me Ch*dai Hoti Hai`",
    "`Runs to Land`",
    "`Nipple Se Tapak Raha Hai Pasina; Bhigi Hui Gaand Aur Lathpath Hai Seena; Aab Tumhi Batao Ghalib; Itni Garmi Mein Koi Kaise Thoke Hasina`",
    "`Jhante Katne Se Ch**t Aur Nikhar Jaati Hai, Ajeeb Gulshan Hai Yeh Jis Me Ujadne Se Bahaar Aati Hai`",
    "`Kabira Khada Bich Bazaar Fut-Fut Kar Roye, Ga*Nd Maar Sab Chal Diyo Paisa Diyo N Koye`",
    "`College Se Nikalte Hi Kitabein Seene Se Laga Leti Ho, Hum Kya Marr Gaye Hain Jo Khud Hi Daba Leti Ho`",
    "`Aaj Fir Unka Dil Dukha Diya Humne, Aaj Fir Unka Dil Dukha Diya Humne, Dekar Ice Cream Ka Naam Andhere Me Fir Se LaNd Chusa Diya Humne`",
    "`Lund Ki Aawaz Ko Damdar Kehte Hain; Fati Choot Ko Bekaar Kehte Hain; Sirf Chodne Ka Nam Mohabbat Nahi Hota; Kissi Ki Yaadon Mein Mutth Marne Ko Bhi Pyaar Kehte Hain🙈`",
]
RAPE_STRINGS = [
     "`Ja pehle Shilajit kha ke aa gandu`",
     "`The user has been successfully raped Gand fat gyi iski`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari v2 bhi hai`",
     "`Rape coming... Raped! haha 😆`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
     "`Ky Re Lodu Fat gyi ky😂`",
     "`Tu Randi hai Sabko pta hai😂`",
     "`Dekhle bhaiyya esa hai! jaat na jalao Gand maar lenge tumhari😂`",
     "`Jaana chodu chad jake land chaat`",
     "`Yaar ajab tere nkhare,gazab tera style hain, gand dhone ki tameez nahi, haath main mobile hai`",
     "`Chodte Chodte Subah Ho Gyi L*nd Mein Pad Gaye Chale, Ch**t Fat Ke Gufa Ho Gyi, Wah Re Ch*dne Wale.`",
] 
ABUSE_STRINGS = [
       "`Madharchod`",
	   "`Gaandu`",
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Ma ka Bhodsa madharchod`",
	   "`mml`",
           "`Chal nikal chutiye😆`",
           "`Arey bhopdike gand me chatta lega ki Dannda 😂`",
           "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",
           "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
           "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
           "`Kahe Rahiman Kaviraaj Ch*Ot Ki Mahima Aisi,La*Nd Murjha Jaaye Par Ch*Ot Waisi Ki Waisi`",
           "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
]
GEY_STRINGS = [
     "`you gey bsdk`",
     "`you gey`",
     "`you gey in the house`",
     "`you chakka`",
     "`you gey gey gey gey gey gey gey gey`",
     "`you gey go away`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Pros here -_- Time to Leave`",
]
INSULT_STRINGS = [ 
    "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 544 section 9 prevents me from replying to stupid humans like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",	
]
CHU_STRINGS = [
     "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
     "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
     "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
     "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
     "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
     "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
     "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
]
# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$")
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern="^-_-$")
async def lol(lel):
    """ Ok... """
    okay = "-_-"
    for _ in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 🅱️
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        reply_text = str(message).translate(WIDE_MAP)
        await vpr.edit(reply_text)


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
            (r"\1"*count),
            message
        )
        await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit(
                "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
            )
            return

        input_text = " ".join(message).lower()
        zalgofied_text = zalgo.zalgo().zalgofy(input_text)
        await zgfy.edit(zalgofied_text)


@register(outgoing=True, pattern="^hi$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit("Hy gandu!😄")
			  
@register(outgoing=True, pattern="^land$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit("Nikal Laude Pehli Fursat Me Nikal!😎")			  
                          
                          
@register(outgoing=True, pattern="^.hack$")
async def hacking (hacked):
    """ Dont Hack Too much -_-"""
    if not hacked.text[0].isalpha() and hacked.text[0] not in ("/", "#", "@", "!"):
        if await hacked.get_reply_message():
            await hacked.edit(
                "`Targeted Account Hacked successfully 😎......`\n"
                "`Pay 1001$ to` @anonycrew `To Remove This Hack...`\n"
            )

			  
@register(outgoing=True, pattern="^.kill$")
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                "`Targeted User was Killed successfully Chal nikal ab Bhosdike😈......`\n"
            )
			  
@register(outgoing=True, pattern="^.bskd(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await owo.edit("` Nikal Laude Pehli Fursat Me Nikal Koi Jarurt Nhi Idhar Teri Bhosdike Pehli Fursat Me nikal Chaderchod Laude! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(FACEREACTS))
        reply_text = FACEREACTS[index]
        await react.edit(reply_text)


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(r"¯\_(ツ)_/¯")


@register(outgoing=True, pattern="^.runs$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    if not DISABLE_RUN:
        if not run.text[0].isalpha() and run.text[0] not in ("/", "#", "@", "!"):
            index = random.randint(0, len(RUNSREACTS) - 1)
            reply_text = RUNSREACTS[index]
            await run.edit(reply_text)


@register(outgoing=True, pattern="^.disable runs$")
async def disable_runs(norun):
    """ Some people don't like running... """
    if not norun.text[0].isalpha() and norun.text[0] not in ("/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = True
        await norun.edit("```Done!```")


@register(outgoing=True, pattern="^.enable runs$")
async def enable_runs(run):
    """ But some do! """
    if not run.text[0].isalpha() and run.text[0] not in ("/", "#", "@", "!"):
        global DISABLE_RUN
        DISABLE_RUN = False
        await run.edit("```Done!```")


@register(outgoing=True, pattern="^.metoo$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(METOOSTR) - 1)
        reply_text = METOOSTR[index]
        await hahayes.edit(reply_text)


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        reply_text = spongemock.mock(message)
        await mock.edit(reply_text)


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)


@register(outgoing=True, pattern="^.bt$")
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await bte.edit(
                "`BLUETEXT MUST CLICK.`\n"
                "`Are you a stupid animal which is attracted to colours?`"
            )
                     
@register(outgoing=True, pattern="^.rape$")
async def raping (raped):
    """ Dont Rape Too much -_-"""
    if not raped.text[0].isalpha() and raped.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(RAPE_STRINGS) - 1)
        reply_text = RAPE_STRINGS[index]
        await raped.edit(reply_text)


@register(outgoing=True, pattern="^.chu$")
async def chutiya (chus):
    """ String for Chu only -_-"""
    if not chus.text[0].isalpha() and chus.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = CHU_STRINGS[index]
        await chus.edit(reply_text)			  
			  
			  
@register(outgoing=True, pattern="^.insult$")
async def insulting (insulted):
    """ Dont Insult Too much -_-"""
    if not insulted.text[0].isalpha() and insulted.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(INSULT_STRINGS) - 1)
        reply_text = INSULT_STRINGS[index]
        await insulted.edit(reply_text)	

			  
@register(outgoing=True, pattern="^.pro$")
async def proo (pros):
    """ String for Pros only -_-"""
    if not pros.text[0].isalpha() and pros.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(PRO_STRINGS) - 1)
        reply_text = PRO_STRINGS[index]
        await pros.edit(reply_text)			  
   
			  
@register(outgoing=True, pattern="^.gey$")
async def geys (geyed):
    """ Use only for gey ppl -_-"""
    if not geyed.text[0].isalpha() and geyed.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(GEY_STRINGS) - 1)
        reply_text = GEY_STRINGS[index]
        await geyed.edit(reply_text)
			  
			  
@register(outgoing=True, pattern="^.abuse$")
async def abusing (abused):
    """ Dont Abuse Too much bsdk -_-"""
    if not abused.text[0].isalpha() and abused.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSE_STRINGS) - 1)
        reply_text = ABUSE_STRINGS[index]
        await abused.edit(reply_text)
                          
                          
@register(pattern='.type(?: |$)(.*)')
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    if not typew.text[0].isalpha() and typew.text[0] not in ("/", "#", "@", "!"):
        textx = await typew.get_reply_message()
        message = typew.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await typew.edit("`Give a text to type!`")
            return
        sleep_time = 0.03
        typing_symbol = "|"
        old_text = ''
        await typew.edit(typing_symbol)
        await asyncio.sleep(sleep_time)
        for character in message:
            old_text = old_text + "" + character
            typing_text = old_text + "" + typing_symbol
            await typew.edit(typing_text)
            await asyncio.sleep(sleep_time)
            await typew.edit(old_text)
            await asyncio.sleep(sleep_time)

CMD_HELP.update({
    "memes": "Ask Thoncc (@Skittles9823Bot) for that."
})
