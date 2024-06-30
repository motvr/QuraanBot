import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()



BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "14911221"))
API_HASH = getenv("API_HASH", "a5e14021456afd496e7377331e2e5bcf")