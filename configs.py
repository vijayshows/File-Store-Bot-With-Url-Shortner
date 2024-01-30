import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8733404"))
  API_HASH = os.environ.get("API_HASH", "f19aed00b0c74abed0359016afc1733f")

  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6898447547:AAFj3fAep2W2O69lilL3jv-TNluMJE9EnyI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "QL_Movie_Links_Bot")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002087036746"))
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  
  #BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925688295:AAFjVjgfg_m1f4Wd6B3AaqBAm8vFkH31guk")
  #BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tamilan_Rocks1_Bot")
  #LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001884285982"))
  #UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001859384286")
  
  #BOT_TOKEN = os.environ.get("BOT_TOKEN", "6529788493:AAFp49RQQTHhv1P3DMxQUMMZUAzvQeWDkP0")
  #BOT_USERNAME = os.environ.get("BOT_USERNAME", "QTL_Series_Bot")
  #LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002119561803"))
  #UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002028128566")

  #BOT_TOKEN = os.environ.get("BOT_TOKEN", "6935162436:AAH9dHsQ-0cpO-JAUi1B_voh0K0dwzqeUB8")
  #BOT_USERNAME = os.environ.get("BOT_USERNAME", "QL_Series_Bot")
  #LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002035253761"))
  #UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002028128566")

  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002087036746")) #QL_Movie_Links_Bot
  #DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002038837206")) #Common
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "ae8999b1a230fee55d762c4682e14321d29f7038")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "807374433"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://leecher:leecher@cluster0.606mkpi.mongodb.net/?retryWrites=true&w=majority")
  
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n
**This is New Movies and Series File Share Bot ✨ To get Instant Updates Please Join Our Main Channel 💯**\n"""
