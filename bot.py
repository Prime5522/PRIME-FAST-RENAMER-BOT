from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from flask import Flask

# Flask অ্যাপ্লিকেশন তৈরি করুন
flask_app = Flask(__name__)

# Pyrogram ক্লায়েন্ট তৈরি করুন
bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

# Pyrogram ক্লায়েন্টের জন্য মিন চ্যাট ও চ্যানেল আইডি সেট করুন
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

# হোমপেজ রাউট
@flask_app.route('/')
def home():
    return "Hello, Renamer Bot is running!"

# মূল কোড
if STRING_SESSION:
    apps = [Client2, bot]
    for app in apps:
        app.start()
    # Flask সার্ভার চালানো একটি আলাদা থ্রেডে
    flask_app.run(host='0.0.0.0', port=8080)
    idle()
    for app in apps:
        app.stop()
else:
    bot.run()
