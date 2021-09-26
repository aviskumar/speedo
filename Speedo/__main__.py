import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Speedo import LOGS, bot, tbot
from Speedo.config import Config
from Speedo.utils import load_module
from Speedo.version import __speedo__ as speedover
hl = Config.HANDLER
SPEEDO_PIC = Config.ALIVE_PIC
# let's get the bot ready
async def speedo_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"SPEEDOBOT_SESSION - {str(e)}")
        sys.exit()


# Speedo starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting Speedo 🔰")
            bot.loop.run_until_complete(speedo_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 Speedo Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "Speedo/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-Speedo/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "Speedo/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your Speedo Is Now Working ⚡")
LOGS.info(
    "Head to @Its_Speedo for Updates. Also join chat group to get help regarding to Speedo."
)

# that's life...
async def speedo_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                SPEEDO_PIC,
                caption=f"#START \n\nDeployed SPEEDOBOT Successfully\n\n**SPEEDOBOT - {speedover}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [SPEEDOBOT Channel](t.me/Its_Speedo) for Updates & [SPEEDOBOT Chat](t.me/Speedo_chat) for any query regarding SPEEDOBOT",
            )
    except Exception as e:
        LOGS.info(str(e))



if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Speedo
