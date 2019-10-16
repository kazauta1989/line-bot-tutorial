# 從 line_bot_api import 全部到 contact.py
from line_bot_api import *


def contact_event(event):
    # TemplateSendMessage - ButtonsTemplate有3個actions
    # PostbackAction 可以在按鈕裡面帶入參數（預約功能會用到）
    # MessageAction 按鈕按下去單純會回傳訊息
    # URIAction 使用者點擊時可以連到網址或是打電話
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # 圖片、標題、說明
            thumbnail_image_url='https://i.imgur.com/izzpeRb.jpg',
            title='聯絡我們',
            text='請選擇',
            actions=[
                URIAction(
                    # label 按鈕名稱
                    # uri 可以填網址也可以填電話
                    label='打給我們',
                    uri='tel:+1234567799'
                )
            ]
        )
    )

    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[buttons_template_message]

    )