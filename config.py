from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 2545223
  API_HASH = "91af3cce4f3e238fd51592eafc7f2f75"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "Ready to abuse"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgresql://postgres:MdrEOgIUutVaRKRAVwSm@containers-us-west-28.railway.app:6916/railway"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  LEGEND_STRING = "AQAQLDyV80zqE5LUqsFizI4T3eE5fo-uOaYRQKgRPIOm4gQ9upoKjRvP2Xoc23H61bYvjoRWgftTgAD3ft8wNtt2wLnvkyEM4UI3d7bjlbdPMw6DpGKLSBUmkt-3hslo6C44XFH9ezWwgLhgYUWLD5zVXLceycjLTIvJvykghUgAlYERWtyahqCU6996wzM7gg52JaWodrKBvQV0NKAKb1AJQE-4C4iFSCiVXyzESHKufqiqcqogkp4teHNyUtP0URzxI_ybEKHtwGAnpxaqHTFlEkJ0txkVxfoeXeT0JAzOiegYT0RAiQkl2y5jG02l41pdRtr9KnMukkOzgPzOqpO6em3gZAA"

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "5139784361:AAFSa-7kvEoPCND_SPr8Qa5-lxx8a4YAJDk" #token
  BOT_USERNAME = "@vikubsbot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -1001686939612

  # Custom Command Handler. 
  COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\."
  #User Command Handler
  HANDLER = os.environ.get("COMMAND_HAND_LER", r"\."
  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = [5042525177]

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,"
