from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = "13197673"
API_HASH = "052ce58975f187e3ab08d9fbaa66dfc8"
BOT_TOKEN = "5621603973:AAHihJK21nsFEoIWJsREfutk5IguUoFmXIY"


app = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
  InlineKeyboardButton("OTT EXPLORER 🕊️", url="https://t.me/+lwYLN-cyVJ1hYzU1"),
  InlineKeyboardButton("MOVIE MAX || HD", url="https://t.me/+t4OM8GE5oGJjNGNl")
  ],[
  InlineKeyboardButton("REQUEST MOVIES GROUP", url="https://t.me/+oSJ17l78prliYzQ1")
  ]]




@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/b72a4501fb93ff4e06ba9.jpg"
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )
        
print("Bot Started")

app.run()

