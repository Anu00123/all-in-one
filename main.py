from pyrogram import Client, filters, errors
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.flood_420 import FloodWait
from configs import cfg
from database import add_user, add_group, all_users, all_groups, users, remove_user
import random, asyncio
from pyrogram.errors import UserNotParticipant


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




#-----broadcast-----
@app.on_message(filters.command("bcast"))
async def bcast_cmd(client, message):
    allusers = users
    lel = await message.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if message.command[0] == "bcast":
                await message.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if message.command[0] == "bcast":
                await message.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")


            

      
print("Bot Started")

app.run()

