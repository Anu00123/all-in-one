from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest, Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from configs import cfg
from database import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
import random, asyncio
import time




gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]



START_BUTTONS = [[
  InlineKeyboardButton("OTT EXPLORER 🕊️", url="https://t.me/+lwYLN-cyVJ1hYzU1"),
  InlineKeyboardButton("MOVIE MAX || HD", url="https://t.me/+t4OM8GE5oGJjNGNl")
  ],[
  InlineKeyboardButton("REQUEST MOVIES GROUP", url="https://t.me/+oSJ17l78prliYzQ1")
  ]]



#----start----
@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/b72a4501fb93ff4e06ba9.jpg",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )



#----users-----
@app.on_message(filters.command("users"))
async def users_cmd(client, message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await message.reply_text(text=f"""
 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)


