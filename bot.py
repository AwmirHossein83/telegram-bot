import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import time
import os

# ===============================
# تنظیمات
# ===============================
#BOT_TOKEN = "8587736496:AAGQdnTPuB_MqFhAxfI1VbLmkt10J47vntg"
TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = "@TrustProxyNet"  # یا آیدی عددی مثل -100xxxxxxxxx

url = "https://api.codebazan.ir/proxy/?type=mtproto"
response = requests.get(url)
data = response.json()  # خروجی وب‌سرویس

SERVER = "188.245.231.85"
PORT = 8443
SECRET =  "eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

#for item in data:
#    SERVER =item['host']
#    PORT = item['port']
#    SECRET = item['secret']

bot = telebot.TeleBot(TOKEN)

# ===============================
# متن پیام
# ===============================
text = f"""Proxy MTProto
Server: {SERVER}
Port: {PORT}
Secret: {SECRET}
"""

# ===============================
# دکمه‌ها (Inline Keyboard)
# ===============================
#keyboard = InlineKeyboardMarkup(row_width=2)

#proxy_url = f"tg://proxy?server={SERVER}&port={PORT}&secret={SECRET}"

#keyboard.add(
#    InlineKeyboardButton("Connect", url=proxy_url),
#    InlineKeyboardButton("Connect", url=proxy_url),
#)

#keyboard.add(
#    InlineKeyboardButton("Connect", url=proxy_url),
#    InlineKeyboardButton("Connect", url=proxy_url),
#)

# ===============================
# ارسال پیام
# ===============================
for item in data:
    SERVER =item['host']
    PORT = item['port']
    SECRET = item['secret']
    text = f"""Proxy MTProto
Server: {SERVER}
Port: {PORT}
Secret: {SECRET}
@TrustProxyNet
"""
    proxy_url = f"tg://proxy?server={SERVER}&port={PORT}&secret={SECRET}"
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
    InlineKeyboardButton("Connect", url=proxy_url),
)
    print(SERVER)
    bot.send_message(
    chat_id=CHANNEL_ID,
    text=text,
    reply_markup=keyboard)
    time.sleep(60)
#bot.send_message(
#    chat_id=CHANNEL_ID,
#    text=text,
#    reply_markup=keyboard
#)