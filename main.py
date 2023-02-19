from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest, Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from configs import cfg
from database import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
import random, asyncio
import time



API_ID = "13197673"
API_HASH = "052ce58975f187e3ab08d9fbaa66dfc8"
BOT_TOKEN = "5621603973:AAHihJK21nsFEoIWJsREfutk5IguUoFmXIY"

app = Client(
    "PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
    )



            

      
print("Bot Started")

app.run()

