from userbot.utils import admin_cmd
from userbot import CmdHelp
from userbot import bot
from userbot.cmdhelp import CmdHelp

@borg.on(admin_cmd(pattern=r"hi ?(.*)")) #initially made by @NOOB_GUY_OP
async def hhi(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\nāāāāāāāā"
    )
# later made by me
@borg.on(admin_cmd(pattern=r"gws ?(.*)"))
async def gws(event):
    giveVar = event.text
    '''m = giveVar[5:-1]
    if not m:'''
    m = " Get Well Soon ! "
    a = giveVar[-1:]
    if a=="s":
        a = "š¹"
    elif not a:
        a = "š¹"
    await event.edit(
        f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m} {a}\n{a}{a}{a}{a}{a}{a}{a}"
    )
@borg.on(admin_cmd(pattern=r"his ?(.*)"))
async def hii(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{b}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}"
    )
@borg.on(admin_cmd(pattern=r"hola ?(.*)"))
async def hlo(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "šŗ"
    b = giveVar[7:8]
    if not b:
        b = "āØ"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}"
    )
@borg.on(admin_cmd(pattern=r"by ?(.*)"))
async def bye(event):
    giveVar = event.text
    a = giveVar[5:6]
    if not a:
        a = "āØ"
    b = giveVar[7:8]
    if not b:
        b = "šŗ"
    await event.edit(                              
        f"ā­āāā³ā®ā±ā±ā­ā³āāāā®\nāā­ā®āā°ā®ā­āÆāā­āāāÆ\nāā°āÆā°ā® {a}ā­ā«ā°āāā®\nāā­{b}ā®ā£ā®ā­āÆāā­āāāÆ\nāā°{b}āÆāāāā±āā°āāā®\nā°āāāāÆā°āÆā±ā°āāāāÆ\n                              LĆŖÉ ĆŖÉ³ĢdįŗĆøā "
    )


CmdHelp("emotes").add_command(
   'hi <emoji>', None, 'Try it yourself' 
).add_command(
   'gws <emoji>', None, 'Try it yourself'
).add_command(
   'hlo1 <emoji>', None, 'Try it yourself'
).add_command(
   'his <emoji>', None, 'Try it yourself'
).add_command(
   'bye <emoji>', None, 'Try it yourself'
).add()
