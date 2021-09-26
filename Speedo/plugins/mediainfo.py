import os

from . import *


@speedo.on(Speedo_cmd(pattern="mediainfo$"))
@speedo.on(sudo_cmd(pattern="mediainfo$", allow_sudo=True))
async def mediainfo(event):
    SPEEDO_MEDIA = None
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "Reply to a media to fetch info...")
    if not reply.media:
        return await eod(event, "Reply to a media file to fetch info...")
    speedo = await eor(event, "`Fetching media info...`")
    SPEEDO_MEDIA = reply.file.mime_type
    if not SPEEDO_MEDIA:
        return await speedo.edit("Reply to a media file to fetch info...")
    elif SPEEDO_MEDIA.startswith(("text")):
        return await speedo.edit("Reply to a media file to fetch info ...")
    hel_ = await mediadata(reply)
    file_path = await reply.download_media(Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        out = "Unknown Format !!"
    paster = f"""
<h2>📃 MEDIA INFO 📃</h2>
<code>
{hel_}
</code>
<h2>🧐 MORE DETAILS 🧐</h2>
<code>
{out} 
</code>"""
    paste = await telegraph_paste(f"{SPEEDO_MEDIA}", paster)
    await speedo.edit(f"📌 Fetched  Media Info Successfully !! \n\n**Check Here :** [{SPEEDO_MEDIA}]({paste})")
    os.remove(file_path)

CmdHelp("mediainfo").add_command(
  "mediainfo", "<reply to a media>", "Fetches the detailed information of replied media."
).add_info(
  "Everything About That Media."
).add_warning(
  "✅ Harmless Module."
).add()
