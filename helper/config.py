#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/wahebtalal/VideoCompressBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID",29452145, cast=int)
    API_HASH = config("API_HASH","5a2784e571fe5043852d32396a34a13b")
    BOT_TOKEN = config("BOT_TOKEN","7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
    OWNER = config("OWNER_ID", default=6169288210, cast=int)
    LOG = config("LOG_CHANNEL",-1002243837012, cast=int)
    GroupName=config("GroupName",default="JXSS")
    GroupUrl=config("GroupUrl","https://t.me/romm207")
    GroupButton = config("GroupButton",default="الانظمام")
    GroupMessage=config("GroupMessage",default="قناة البوت")

    BlockUrl = config("BlockUrl",default="t.me/wahiebtalal")
    BlockButton = config("BlockButton", default="المسؤول")
    BlockMessage = config("BlockMessage", default="تم حضرك من استخدام البوت")
    block=config("Block",default="1 2")

except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
