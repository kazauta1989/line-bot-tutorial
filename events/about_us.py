# 從 line_bot_api import 全部到 about_us.py
from line_bot_api import *


def about_us_event(event):
    about_us_text = '歡迎來到尚尚清潔家'
    about_us_img = 'https://i.imgur.com/6bR33SV.png'
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=about_us_text),
         ImageSendMessage(original_content_url=about_us_img, preview_image_url=about_us_img),
         StickerSendMessage(package_id='11537', sticker_id='52002763')
         ])
