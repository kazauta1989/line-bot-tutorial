# import 所需套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    '617X/r7VBmoBeh+guL9HTBkWQ10b7jRVZKPme8BQOqtjic8MPVfacmNE0EkB+rNigcDPsX0PvqNxam55wUuYIrudgWKTWhONJX5c4knZQS+8M0dre/vx24auZR5QZGUxIOPhT8ZpOihn7neASRPxxwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('681b3abaab63d98ea984dd76a7215b33')


# 監聽所有來自 /callback 的 Post Request
# /callback路徑，到時候line所傳送的資料到WebhookUrl就會視為從這裡進來的
# 所以他會取得signature 和 body
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    # 接著把signature 和 body 丟給handler去做處理
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 當handler接受到訊息之後，他會呼叫handle_message這個函式
# 並把event這個物件給丟進來
# 這event物件裡面包含token ： 是哪一個使用者傳送的訊息，以及傳送什麼訊息，都會在event物件裡面

# 透過line_bot_api去回傳event物件裡面的token以及文字訊息
# 擷取event的message.text訊息回傳給使用者
# 簡單說 handle_message(event)這個函式，做的就是使用者傳hi，機器人就回傳一樣的字
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當接收到訊息的時候，會先將訊息變換成小寫
    message_text = str(event.message.text).lower()
    # 當message_text等同於'＠關於我們'時，會回傳line_bot_api.reply_message(）裡的值
    # 另外，當有用到TextSendMessage、ImageSendMessage、VideoSendMessage、等等...
    # 多個Message objects時，要記得用成陣列，才會一次訊息同時送出
    if message_text == '＠關於我們':
        about_us_text = '歡迎來到上上清潔家'
        about_us_img = 'https://i.imgur.com/6bR33SV.png'
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=about_us_text),
         ImageSendMessage(original_content_url=about_us_img, preview_image_url=about_us_img)
         ])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
