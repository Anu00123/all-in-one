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
  ]]




@app.on_message(filters.command("start")
async def op(client, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/b72a4501fb93ff4e06ba9.jpg",
        Caption="👋HELLO I AM MOVIE MAX CHANNEL BOT. can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission")

print("Bot Started"

app.run()

