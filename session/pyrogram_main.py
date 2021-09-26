
import logging
import os
import platform

import pyrogram
from pyrogram import __version__
from bot_utils_files.Localization.engine import Engine
from database.localdb import check_lang
from .pyrogram import (
    Speedo,
    Speedo2,
    Speedo3,
    Speedo4,
    bot,
    speedo_version,
    mongo_client,
)
from main_start.core.startup_helpers import (
    load_plugin,
    load_xtra_mod,
    plugin_collecter,
    run_cmd,
    update_it
)

from .config_var import Config


async def mongo_check():
    """Check Mongo Client"""
    try:
        await mongo_client.server_info()
    except BaseException as e:
        logging.error("Something Isn't Right With Mongo! Please Check Your URL")
        logging.error(str(e))
        quit(1)


async def load_unofficial_modules():
    """Load Extra Plugins."""
    logging.info("Loading X-Tra Plugins!")
    await run_cmd(f'bash bot_utils_files/other_helpers/xtra_plugins.sh {Config.XTRA_PLUGINS_REPO}')
    xtra_mods = plugin_collecter("./xtraplugins/")
    for mods in xtra_mods:
        try:
            load_xtra_mod(mods)
        except Exception as e:
            logging.error(
                "[USER][XTRA-PLUGINS] - Failed To Load : " + f"{mods} - {str(e)}"
            )


async def fetch_plugins_from_channel():
    """Fetch Plugins From Channel"""
    try:
        async for message in Speedo.search_messages(
            Config.PLUGIN_CHANNEL, filter="document", query=".py"
        ):
            hmm = message.document.file_name
            if not os.path.exists(os.path.join("./plugins/", hmm)):
                await Speedo.download_media(message, file_name="./plugins/")
    except BaseException as e:
        logging.error(f"Failed! To Install Plugins From Plugin Channel Due To {e}!")
        return
    logging.info("All Plugins From Plugin Channel Loaded!")


async def run_bot():
    try:
        await update_it()
    except:
        pass
    """Run The Bot"""
    await mongo_check()
    if bot:
        await bot.start()
        bot.me = await bot.get_me()
        assistant_mods = plugin_collecter("./assistant/")
        for mods in assistant_mods:
            try:
                load_plugin(mods, assistant=True)
            except Exception as e:
                logging.error("[ASSISTANT] - Failed To Load : " + f"{mods} - {str(e)}")
    await Speedo.start()
    Speedo.me = await Speedo.get_me()
    Speedo.selected_lang = await check_lang()
    LangEngine = Engine()
    LangEngine.load_language()
    Speedo.has_a_bot = bool(bot)
    if Speedo2:
        await Speedo2.start()
        Speedo2.me = await Speedo2.get_me()
        Speedo2.has_a_bot = True if bot else False
    if Speedo3:
        await Speedo3.start()
        Speedo3.me = await Speedo3.get_me()
        Speedo3.has_a_bot = bool(bot)
    if Speedo4:
        await Speedo4.start()
        Speedo4.me = await Speedo4.get_me()
        Speedo4.has_a_bot = bool(bot)
    if Config.PLUGIN_CHANNEL:
        await fetch_plugins_from_channel()
    needed_mods = plugin_collecter("./plugins/")
    for nm in needed_mods:
        try:
            load_plugin(nm)
        except Exception as e:
            logging.error("[USER] - Failed To Load : " + f"{nm} - {str(e)}")
    if Config.LOAD_UNOFFICIAL_PLUGINS:
        await load_unofficial_modules()
    full_info = f"""Speedo Based On Pyrogram V{__version__}
Python Version : {platform.python_version()}
Speedo Version : {speedo_version}
You Can Visit @SpeedoSupportOfficial For Updates And @SpeedoChat For Any Query / Help!
"""
    logging.info(full_info)
    await pyrogram.idle()


if __name__ == "__main__":
    Speedo.loop.run_until_complete(run_bot())
