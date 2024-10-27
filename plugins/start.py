from datetime import date as date_
import os, re, datetime, random, asyncio, time, humanize
from script import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.progress import humanbytes
from helper.database import botdata, find_one, total_user
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from config import *

token = BOT_TOKEN
botid = token.split(':')[0]





@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
    
    try:
        id = message.text.split(' ')[1]
    except IndexError:
        id = None

    loading_sticker_message = await message.reply_sticker("CAACAgUAAxkBAAJ_9GcBHjuwkFd321YlOG4WOtdDCLv7AAIhFAACTiwJVPNa_9D21RH6NgQ")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    
    text = f"""{message.from_user.mention} \nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ʀᴇɴᴀᴍᴇʀ  ᴀɴᴅ  ᴄᴏɴᴠᴇʀᴛᴇʀ  ʙᴏᴛ  ᴡɪᴛʜ  ᴘᴇʀᴍᴀɴᴇɴᴛ  ᴀɴᴅ  ᴄᴜsᴛᴏᴍ  ᴛʜᴜᴍʙɴᴀɪʟ  sᴜᴘᴘᴏʀᴛ.\n\nᴊᴜsᴛ  sᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ᴠɪᴅᴇᴏ  ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ !!\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/Prime_Botz">𝐏𝐑𝐈𝐌𝐄 𝐁𝐎𝐓𝐳 🔥</a></blockquote></b>"""
    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Updates", url="https://t.me/Prime_botz"),
        InlineKeyboardButton("💬 Support", url="https://telegram.me/Prime_Admin_Support_ProBot")],
        [InlineKeyboardButton("🛠️ Help", callback_data='help'),
        InlineKeyboardButton("❤️‍🩹 About", callback_data='about')],
        [InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url="https://telegram.me/Prime_Nayem")]
        ])
    
    await message.reply_photo(
        photo=START_PIC,
        caption=text,
        reply_markup=button,
        quote=True
        )
    return    



@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))

    user_id = message.from_user.id    
    if FORCE_SUBS:
        try:
            await client.get_chat_member(FORCE_SUBS, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]

            # এখানে ছবির URL যুক্ত করুন
            photo_url = "YOUR_PHOTO_URL_HERE"  # ছবির URL এখানে যুক্ত করুন

            # ছবিটি এবং নতুন ক্যাপশন সহ টেক্সট পাঠানোর কোড
            await client.send_photo(
                chat_id=user_id, 
                photo=photo_url,
                caption="Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ ғɪʀꜱᴛ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ\n\nғɪʀꜱᴛ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '✇ Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇' ʙᴜᴛᴛᴏɴ, ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ 'ʀᴇᴏ‌ᴜᴇꜱᴛ ᴛᴏ Jᴏɪɴ' ʙᴜᴛᴛᴏɴ.\n\nᴀғᴛᴇʀ ᴛʜᴀᴛ ᴄᴏᴍᴇ ʜᴇʀᴇ ᴀɢᴀɪɴ ᴀɴᴅ ꜱᴇɴᴅ ʏᴏᴜʀ ғɪʟᴇ",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✇ Join Our Updates Channel ✇", url=f"https://t.me/{FORCE_SUBS}")]
                ])
            )

            # লগ চ্যানেলে বার্তা পাঠানোর কোড
            await client.send_message(LOG_CHANNEL, f"<b><u>New User Started The Bot</u></b> \n\n<b>User ID :</b> <code>{user_id}</code> \n<b>First Name :</b> {message.from_user.first_name} \n<b>Last Name :</b> {message.from_user.last_name} \n<b>User Name :</b> @{message.from_user.username} \n<b>User Mention :</b> {message.from_user.mention} \n<b>User Link :</b> <a href='tg://openmessage?user_id={user_id}'>Click Here</a> \n<b>User Plan :</b> {user}")
            return
        
    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    user_deta = find_one(user_id)
    used_date = user_deta["date"]
    buy_date = user_deta["prexdate"]
    daily = user_deta["daily"]
    user_type = user_deta["usertype"]

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 120
    else:
        LIMIT = 10
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    
    if left > 0:
        await message.reply_text(f"<b>Sorry Dude I Am Not Only For You \n\nFlood Control Is Active So Please Wait For {ltime} </b>", reply_to_message_id=message.id)
    else:
        # আপনার অন্যান্য কোড এখানে থাকবে
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        file_id = file.file_id
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% Of Daily {humanbytes(limit)} Data Quota Exhausted.\n\n<b>File Size Detected :</b> {humanbytes(file.file_size)}\n<b>Used Daily Limit :</b> {humanbytes(used)}\n\nYou Have Only <b>{humanbytes(remain)}</b> Left On Your Account.\n\nIf U Want To Rename Large File Upgrade Your Plan", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
            return
        if value < file.file_size:
            
            if STRING_SESSION:
                if buy_date == None:
                    await message.reply_text(f"You Can't Upload More Than 2GB File.\n\nYour Plan Doesn't Allow To Upload Files That Are Larger Than 2GB.\n\nUpgrade Your Plan To Rename Files Larger Than 2GB.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__What Do You Want Me To Do With This File ?__\n\n**File Name :** `{filename}`\n**File Size :** {humanize.naturalsize(file.file_size)}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename 📝", callback_data="rename"), InlineKeyboardButton("✖️ Cancel ✖️", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Your Plan Expired On {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("You Can't Upload More Than 2GB File.\n\nYour Plan Doesn't Allow To Upload Files That Are Larger Than 2GB.\n\nUpgrade Your Plan To Rename Files Larger Than 2GB.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
            
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__What Do You Want Me To Do With This File ?__\n\n**File Name :** `{filename}`\n**File Size :** {filesize}\n**DC ID :** {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rename 📝", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cancel ✖️", callback_data="cancel")]]))
