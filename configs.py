# (c) @AbirHasan2005

import os
from os import environ

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))


class Config(object):
  DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
  API_ID = int(os.environ.get("API_ID", "18860540"))
  API_HASH = os.environ.get("API_HASH", "22dd2ad1706199438ab3474e85c9afab")
  BOT_TOKEN = os.environ.get("BOT_TOKEN","")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "5766"))
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6887"))
  DATABASE_URL = os.environ.get("DATABASE_URL","")
  VERIFY_KEY = os.environ.get("VERIFY_KEY", "").split()#set plz don't use special character like @#$%* etc us only letter number and = ,To use this EARNING var value must be true.multiple key separted by space,if u want to use pre shorted link then verify_key and verify_link must be at same index. example if 'unfhd" this key is related to https://www.shorted.link then and verify_key is at index 1 in string(separated by space) then verify_link must be at index 1 in verify_link string
  VERIFY_LINK = os.environ.get("VERIFY_LINK","").split()#To use this EARNING var value must be True. multiple verification link separted by space. these links can be shorted links which is all related to VERIFY_KEY 
  EARNING = bool(os.environ.get("EARNING",False))#If this is True then ---- 1.SHORTNER_API_LINK and SHORTNER_API must be fill if VERIFY_KEY not filled, 2. if VERIFY_KEY is filled then SHORTNER_API & SHORTNER_API_LINK must not filled
  VERIFY_DURATION = (os.environ.get("VERIFY_DURATION",""))
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
  BANNED_USERS = set(
    int(x) for x in os.environ.get("BANNED_USERS", "1236848594").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
  BANNED_CHAT_IDS = list(
    set(
      int(x)
      for x in os.environ.get("BANNED_CHAT_IDS", "-1007947838838").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  SHORTNER_API_LINK = os.environ.get("SHORTNER_API_LINK", None)
  SHORTNER_API = os.environ.get("SHORTNER_API", None)
  REMOVE_WORD = os.environ.get("REMOVE_WORD","")#multiple word must be separted by '|'
  SEND_PHOTO = os.environ.get("SEND_PHOTO", "")
  ADD_DETAIL = os.environ.get("ADD_DETAIL", "")
  SHORT_SINGLE_LINK = bool(os.environ.get("SHORT_SINGLE_LINK",False))
  HOW_TO_VERIFY_LINK = os.environ.get("HOW_TO_VERIFY_LINK","")
  ABOUT_BOT_TEXT = f"""
This is Permanent Files and text Store Bot!
Send me any file or text, I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files and test Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** "IDK😎"

🧑🏻‍💻 **Developer:** "Berojgaar 😂"

👥 **Support Group:** "not need 🤓"

📢 **Updates Channel:** "not need💀"
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** ☠️

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/) (PayPal)
"""
  HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
