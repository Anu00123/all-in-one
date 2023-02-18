from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest, Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from configs import cfg
from database import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
import random, asyncio
import time
from helper_func import subscribed



API_ID = "13197673"
API_HASH = "052ce58975f187e3ab08d9fbaa66dfc8"
BOT_TOKEN = "5621603973:AAHihJK21nsFEoIWJsREfutk5IguUoFmXIY"

app = Client(
    "PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
    )




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
@app.on_message(filters.command("start") & filters.private & subscribed)
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





#------Autoaprove--------

@app.on_chat_join_request(filters.group | filters.channel)
async def approve(client, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    try:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        add_group(chat.id)
        img = random.choice(gif)
        await client.send_video(chat_id=user.id, video=img)
        add_user(user.id)
    except Exception as err:
        print(str(err))



#-------helpCommand--------

@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/b72a4501fb93ff4e06ba9.jpg",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )




#-------ping------

@app.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")





#------FSUB-------






            

      
print("Bot Started")

app.run()

