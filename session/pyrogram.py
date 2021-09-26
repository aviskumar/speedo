
import logging
import os
import time
import motor.motor_asyncio
from pyrogram import Client

from .config_var import Config

# Note StartUp Time - To Capture Uptime.
start_time = time.time()
speedo_version = "0.1"

# Enable Logging For Pyrogram
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [Speedo] - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)


mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.MONGO_DB)

CMD_LIST = {}
XTRA_CMD_LIST = {}
sudo_id = Config.AFS

if not Config.STRINGSESSION:
    logging.error("No String Session Found! Speedo is Exiting!")
    quit(1)

if not Config.API_ID:
    logging.error("No Api-ID Found! Speedo is Exiting!")
    quit(1)

if not Config.API_HASH:
    logging.error("No ApiHash Found! Speedo is Exiting!")
    quit(1)

if not Config.LOG_GRP:
    logging.error("No Log Group ID Found! Speedo is Exiting!")
    quit(1)


# Clients - Upto 4 Clients is Supported!
if Config.STRINGSESSION:
    Speedo = Client(
        Config.STRINGSESSION,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
if Config.STRINGSESSION_2:
    Speedo2 = Client(
        Config.STRINGSESSION_2,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Speedo2 = None
if Config.STRINGSESSION_3:
    Speedo3 = Client(
        Config.STRINGSESSION_3,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Speedo3 = None
if Config.STRINGSESSION_4:
    Speedo4 = Client(
        Config.STRINGSESSION_4,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=180,
    )
else:
    Speedo4 = None

if Config.BOT_TOKEN:
    bot = Client(
        "MyAssistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        sleep_threshold=180,
    )
else:
    bot = None
