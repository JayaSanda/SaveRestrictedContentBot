#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "21767556"
API_HASH = "80e2ef1f848ffdd325c0a87592dc33ca"
BOT_TOKEN = "6448020230:AAH2HYzuIN2pFgKSzDYw8avLDkZgVhtS7iQ"
SESSION = "BQFMJYQAw64ixXjHDiFgafpX-AK3_9qUZEmvhEDvgHj2M7JiNWhB1Fv3zjcXtahasvw-JjKvT7P-K301ophNBisaJqc638cZQysO1BLWBMneLxrUGSPa0dwXhay1j3qJXz9f6LgO6DdLjbGUCxHzts4mvEw-SjA2KwMG6MgiZUTuFe8O5nxukF_wdJPS3a7WDDHh8QvdH9yp_33z76nSpYmAH6dP7tjjstAKO9sz880vr_1pxgdShm8-kZQhdr_RjQqWBN7fbK_7yNhR0g96HfFV7txalZbz6DMwfiwoZFfiRAjJxDdIo-83wK9evjOAvzSBanfdmKay50-6EfVb7Mkoe9x04QAAAAF4bd81AQ"
FORCESUB = "FORCESUB"
AUTH = "5832344086"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
