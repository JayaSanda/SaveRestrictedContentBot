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
SESSION = "BQFMJYQAmkIfPHKvtvgUBC2-snNuDcDDB5dJT25nonoZWihOvmi7hnHqWqa3oQDwqamjiqIddvSaDzUxRc-Mv9qe6DAmxlAUOWEqkQW3Hi6UNepC3291faWu6WTg1DxBy-CQr4jO49FLyGdcYGk64MUUwvpc4rhAb45Hb6rcsoBMHCkRWw2wI5hTSrkI0nAG_ytfDXTF2R8YKPgbQQHa46MY9lPdL7jcdNNtUf7FCXc8aKj2_YWg9h5uR_-PQnnULkCBOFEVWGNHy4TrCDwfOC1hbXy6zEZSkaVNeru43bN3E7Zx8zvpguIjG6aAHlmhsX5tGzyJO1BaL18ICPvu-pM6qckm2gAAAAFbooIWAA"
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
