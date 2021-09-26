from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

speedo_pic = Config.ALIVE_PIC or "https://telegra.ph/file/f46b11140c307df13750d.jpg"
alive_c = f"__**🔥🔥Speedo ɨs օռʟɨռɛ🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {speedo_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• SPEEDOBOT       :  __**{speedo_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {speedo_channel}\n"

#-------------------------------------------------------------------------------

@speedo.on(Speedo_cmd(outgoing=True, pattern="speedo$"))
@speedo.on(sudo_cmd(pattern="speedo$", allow_sudo=True))
async def up(speedo):
    if speedo.fwd_from:
        return
    await speedo.get_chat()
    await speedo.delete()
    await bot.send_file(speedo.chat_id, speedo_pic, caption=alive_c)
    await speedo.delete()

msg = f"""
**⚡ 𝒮𝒫𝐸𝐸𝒟𝒪 ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**SPEEDOBOT  :**  **{speedo_ver}**
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@speedo.on(Speedo_cmd(pattern="alive$"))
@speedo.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def speedo_a(event):
    try:
        speedo = await bot.inline_query(botname, "alive")
        await speedo[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "speedo", None, "Shows the Default Alive Message"
).add_command(
  "alive", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
