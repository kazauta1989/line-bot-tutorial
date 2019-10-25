# 從 line_bot_api import 全部到 location.py
from line_bot_api import *


def quick_reply_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hello, world',
                        quick_reply=QuickReply(
                            items=[
                                QuickReplyButton(action=MessageAction(label="測試", text="文字"))
                            ]))
    )
