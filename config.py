from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 6235351
  API_HASH = "f68fde1378da8f85a243f2ae57f2fcf9"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "Ready to abuse"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgresql://postgres:LaTuzQax2tcohQIZSoJm@containers-us-west-16.railway.app:5533/railway" 
  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  LEGEND_STRING = "1BJWap1wBuzdeTXB6rRs-AhQYYSl0NApctmdr39ZCTNyjizmpc2ljLOU8gsy_6LT4cl6bpnNID8ThtGg9K6k9-cJ4KOhJx986CFrWfJMq3dEmac9kOxFBGFK5UFN2dpszWEOX-17kDz1idx5mrKM8-zBSdylR842xGLB0ZMknvCquBPA0pchTcakLZxykMuzbUcl2thv6yvZrlwnEqVTAqqiqWSCslKdnyREQEO8QOw41y2UaCmajx4yK9dl1pbVrX7NtrKV_Nzb0Xad-qRnulXVywKjLwO1UTv2l7cejPIFkhgpVkrjMWHy_T1t8Az4Z_jD-1gwrMDoR_3zXLrlR8aa5eh-rzzU="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "5139784361:AAFSa-7kvEoPCND_SPr8Qa5-lxx8a4YAJDk" #token
  BOT_USERNAME = "@vikubsbot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -1001760151544

  # Custom Command Handler. 
  COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\."
  #User Command Handler
  HANDLER = os.environ.get("COMMAND_HAND_LER", r"\."
  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,"
