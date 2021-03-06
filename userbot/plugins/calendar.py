"""Malayalam Calendar plugin for @UniBorg
SYNTAX: .calendar YYYY-MM-DD"""
from telethon import events
import asyncio
from datetime import datetime
import requests
import json
from userbot.utils import admin_cmd
from userbot import CmdHelp
from . import *

@borg.on(admin_cmd(pattern="calendar (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(".")
    if len(input_sgra) == 3:
        yyyy = input_sgra[0]
        mm = input_sgra[1]
        dd = input_sgra[2]
        required_url = "https://calendar.kollavarsham.org/api/years/{}/months/{}/days/{}?lang={}".format(yyyy, mm, dd, "en")
        headers = {"Accept": "application/json"}
        response_content = requests.get(required_url, headers=headers).json()
        a = ""
        if "error" not in response_content:
            current_date_detail_arraays = response_content["months"][0]["days"][0]
            a = json.dumps(current_date_detail_arraays, sort_keys=True, indent=4)
        else:
            a = response_content["error"]
        await event.edit(str(a))
    else:
        await event.edit("SYNTAX: .calendar YYYY.MM.DD")
    end = datetime.now()
    ms = (end - start).seconds

CmdHelp("calender").add_command(
   'calender', None, '.calender YYYY.MM.DD To Show Calender'
).add() 
