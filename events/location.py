# 從 line_bot_api import 全部到 location.py
from line_bot_api import *


def location_event(event):
    title_text = '尚尚清潔家地址'
    address_text = '414台中市烏日區中華路385巷16號'
    latitude = 24.110664
    longitude = 120.637629
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title=title_text, address=address_text, latitude=latitude, longitude=longitude)
    )
